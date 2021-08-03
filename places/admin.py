from django.contrib import admin

# Register your models here.
from .models import Place, Image

# admin.site.register(Place)
# admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    verbose_name_plural = 'Фотографии'
    fieldsets = ((None, {'fields': ('img', 'position',)}),)
    extra = 1


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
