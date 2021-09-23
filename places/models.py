from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description_short = models.TextField(verbose_name='Краткое описание', blank=True)
    description_long = HTMLField(verbose_name='Полное описание', blank=True)
    coordinates_lng = models.FloatField(verbose_name='Долгота')
    coordinates_lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    position = models.IntegerField(default=0, verbose_name='Позиция', null=True)
    img = models.ImageField(verbose_name='Картинка')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место', related_name='place_images')

    class Meta(object):
        ordering = ['position']

    def __str__(self):
        return f'{str(self.position)} {self.place.title}'
