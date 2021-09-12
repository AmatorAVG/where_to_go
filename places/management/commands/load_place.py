#  комманда для загрузки новых локаций из json файлов
import requests
from urllib.parse import urlparse
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('links', nargs='+', type=str)

    def handle(self, *args, **options):
        for link in options['links']:
            r = requests.get(link)
            r.raise_for_status()
            geo_json_dict = r.json()
            place, created = Place.objects.get_or_create(title=geo_json_dict['title'],
                                                         defaults={'description_short': geo_json_dict['description_short'],
                                                                   'description_long': geo_json_dict['description_long'],
                                                                   'coordinates_lng': geo_json_dict['coordinates']['lng'],
                                                                   'coordinates_lat': geo_json_dict['coordinates']['lat']})
            for img_url in geo_json_dict['imgs']:
                name = urlparse(img_url).path.split('/')[-1]
                resp_img = requests.get(img_url)
                resp_img.raise_for_status()
                content = ContentFile(resp_img.content)
                new_img = Image(place=place)
                new_img.img.save(name, content, save=True)
                new_img.save()
