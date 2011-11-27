from django.contrib import admin
from django.contrib.contenttypes import generic
from models import *
from genericcollection import GenericCollectionTabularInline
from django.conf import settings

class InlineGalleryItem(GenericCollectionTabularInline):
        model = GalleryItem

class GalleryItemInline(generic.GenericStackedInline):
    model = GalleryItem

class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        InlineGalleryItem,
    ]
    
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

class VideoInline(admin.StackedInline):
	model = Video

class GIAdmin(admin.ModelAdmin):
	inlines = [
        VideoInline
    ]


admin.site.register(Project)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryItem)#, GIAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoFormat)
admin.site.register(Image)