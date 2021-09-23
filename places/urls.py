from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'places'
urlpatterns = [
    path('', views.show_main, name='index'),
    path('places/<int:place_id>/', views.place_view, name='places_show'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
