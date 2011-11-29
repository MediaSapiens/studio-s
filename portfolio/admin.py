from django.contrib import admin
from django.contrib.contenttypes import generic
from models import *
from genericcollection import GenericCollectionTabularInline
from django.conf import settings

class InlineGalleryItem(GenericCollectionTabularInline):
        model = GalleryItem
        sortable_field_name = "position"

class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        InlineGalleryItem,
    ]
    sortable_field_name = "position"
    
    class Media:
        js = (settings.MEDIA_URL + 'js/genericcollections.js',)

class VideoFormatInline(admin.StackedInline):
	model = VideoFormat

class VideoAdmin(admin.ModelAdmin):
	inlines = [
        VideoFormatInline,
    ]

class ImageInline(admin.StackedInline):
	model = Image



admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryItem)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoFormat)
admin.site.register(Image)