from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = HTMLField(verbose_name='Полное описание')
    coordinates_lng = models.FloatField(default=0.00, verbose_name='Долгота')
    coordinates_lat = models.FloatField(default=0.00, verbose_name='Широта')


    def __str__(self):
        return self.title


class Image(models.Model):
    position = models.IntegerField(default=0, verbose_name='Позиция')
    img = models.ImageField(max_length=255, verbose_name='Картинка')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место')

    def __str__(self):
        return f'{str(self.position)} {self.place.title}'

    class Meta(object):
        ordering = ['position']