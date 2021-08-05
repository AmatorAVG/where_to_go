from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# Register your models here.
from .models import Place, Image
from adminsortable2.admin import SortableInlineAdminMixin
# admin.site.register(Place)
# admin.site.register(Image)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    verbose_name_plural = 'Фотографии'
    fieldsets = ((None, {'fields': ('img', 'get_preview', 'position',)}),)
    extra = 0
    readonly_fields = ('get_preview',)

    def get_preview(self, obj):
        return format_html('<img src="{}" height={}/>', mark_safe(obj.img.url), 200,)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
