from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from places.models import Place
from django.urls import reverse


def show_main(request):
    places = Place.objects.all()

    geo_json = {
      "type": "FeatureCollection",
      "features": []
    }

    for place in places:
        geo_json["features"].append({"type": "Feature",
                                      "geometry": {
                                          "type": "Point",
                                          "coordinates": [place.coordinates_lng, place.coordinates_lat]
                                      },
                                      "properties": {
                                          "title": place.title,
                                          "detailsUrl": reverse('places:places_show', args=[place.id]),
                                      }
                                      })

    return render(request, 'places/index.html', context={"geo_json": geo_json})


def place_view(request, id):

    place = get_object_or_404(Place, pk=id)

    data_json = {
        "title": place.title,
        "imgs": [img_obj.img.url for img_obj in place.image_set.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": str(place.coordinates_lng),
            "lat": str(place.coordinates_lat)
        }
    }

    return JsonResponse(data_json, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
