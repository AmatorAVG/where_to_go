from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description_short = models.CharField(max_length=255, verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    coordinates_lng = models.FloatField(default=0.00, verbose_name='Долгота')
    coordinates_lat = models.FloatField(default=0.00, verbose_name='Широта')
    # placeId = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class Image(models.Model):
    position = models.IntegerField(verbose_name='Позиция')
    img = models.ImageField(max_length=255, verbose_name='Картинка')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место')

    def __str__(self):
        return str(self.position) + " " + self.place.title
