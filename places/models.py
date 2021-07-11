from django.db import models


# class Image(models.Model):
#     path = models.CharField(max_length=255)


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    coordinates_lng = models.FloatField(default=0.00)
    coordinates_lat = models.FloatField(default=0.00)
    # imgs = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.title