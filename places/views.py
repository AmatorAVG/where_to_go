from django.shortcuts import render
from places.models import Place


def show_main(request):
    places = Place.objects.all()

    data_json = {
      "type": "FeatureCollection",
      "features": []
    }

    for place in places:
        data_json["features"].append({"type": "Feature",
                                      "geometry": {
                                          "type": "Point",
                                          "coordinates": [place.coordinates_lng, place.coordinates_lat]
                                      },
                                      "properties": {
                                          "title": place.title,
                                          "placeId": place.placeId,
                                          "detailsUrl": "./static/places/" + place.placeId + ".json"
                                      }
                                      })

    return render(request, 'places/index.html', context={"value": data_json})
