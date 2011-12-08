import uuid, os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType, ContentTypeManager
from django.contrib.contenttypes import generic

CONTENTTYPES = [u'image', 'video', 'image']

class MediaManager(ContentTypeManager):
    def get_query_set(self):
        return super(MediaManager, self).get_query_set()\
            .filter(app_label='portfolio')

class MediaContentType(ContentType):
    objects = MediaManager()

def images(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images', filename)


class Gallery(models.Model):
    title = models.CharField(_('Gallery title'), max_length=255)
    description = models.TextField(blank=True,null=True)
    media = generic.GenericRelation("GalleryItem", related_name="media")
    position = models.PositiveSmallIntegerField("Position")

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return self.title



class GalleryItem(models.Model):
    gallery = models.ForeignKey(Gallery)
    context = models.TextField(blank=True,null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = generic.GenericForeignKey(ct_field="content_type", fk_field="object_id")
    position = models.PositiveSmallIntegerField("Position", default=0)

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return 'Gallery "%s" %s' % (self.gallery.title,self.content_type.model)

class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True,null=True)

    def __unicode__(self):
        return 'Image #%d' % self.pk 

class Video(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)

    def __unicode__(self):
        return 'Video #%d' % self.pk 

class VideoFormat(models.Model):
    format = models.CharField(_('Video format'), default='720p',max_length=255, blank=True,null=True)
    video_file = models.FileField(upload_to='videos', blank=True,null=True)
    video = models.ForeignKey("Video")

    def __unicode__(self):
        return 'Video Format #%d' % self.pk