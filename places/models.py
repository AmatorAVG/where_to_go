from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    coordinates_lng = models.FloatField(default=0.00)
    coordinates_lat = models.FloatField(default=0.00)
    placeId = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class Image(models.Model):
    position = models.IntegerField()
    img = models.ImageField(max_length=255)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.position) + " " + self.place.title
