from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'places'
urlpatterns = [
    path('', views.show_main, name='index'),
    path('places/<int:id>/', views.place_view, name='places'),
    # path('login/', views.LoginView, name='login'),
    # re_path(r'^login\/.*$', views.test),
    # path('signup/', views.SignupView, name='signup'),
    # path('ask/', views.question_add, name='ask'),
    # path('popular/', views.PopularView, name='popular'),
    # path('new/', views.test, name='new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
