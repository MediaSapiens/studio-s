import uuid, os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType, ContentTypeManager
from django.contrib.contenttypes import generic

CONTENTTYPES = ['video', 'image']

class MediaManager(ContentTypeManager):
    def get_query_set(self):
        return super(ContentTypeManager, self).get_query_set().filter(name__in=CONTENTTYPES)

##class MediaContentType(ContentType):
##    objects = MediaManager()

def images(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images', filename)

class Project(models.Model):
    title = models.CharField(_('Project title'), max_length=255,blank=True,null=True)

class Gallery(models.Model):
    project = models.ForeignKey("Project")
    title = models.CharField(_('Gallery title'), max_length=255)
    description = models.TextField(blank=True,null=True)
    media = generic.GenericRelation("GalleryItem", related_name="media")

class GalleryItem(models.Model):
    gallery = models.ForeignKey(Gallery)
    context = models.TextField(blank=True,null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = generic.GenericForeignKey(ct_field="content_type", fk_field="object_id")

class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True,null=True)

class Video(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)

class VideoFormat(models.Model):
    format = models.CharField(_('Video format'), default='720p',max_length=255, blank=True,null=True)
    video_file = models.FileField(upload_to='videos', blank=True,null=True)
    video = models.ForeignKey("Video")