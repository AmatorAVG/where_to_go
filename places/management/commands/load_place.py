#  комманда для загрузки новых локаций из json файлов
import requests
from urllib.parse import urlparse
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('link', nargs='+', type=str)

    def handle(self, *args, **options):
        for link in options['link']:
            r = requests.get(link)
            r.raise_for_status()
            json_file = r.json()
            place, created = Place.objects.get_or_create(title=json_file['title'],
                                                             description_short=json_file['description_short'],
                                                             description_long=json_file['description_long'],
                                                             coordinates_lng=json_file['coordinates']['lng'],
                                                             coordinates_lat=json_file['coordinates']['lat'])
            for img_url in json_file['imgs']:
                name = urlparse(img_url).path.split('/')[-1]
                requests.get(img_url).raise_for_status()
                content = ContentFile(requests.get(img_url).content)
                new_img = Image(place=place)
                new_img.img.save(name, content, save=True)
                new_img.save()
