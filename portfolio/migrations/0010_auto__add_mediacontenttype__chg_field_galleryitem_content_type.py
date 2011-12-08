# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MediaContentType'
        db.create_table('portfolio_mediacontenttype', (
            ('contenttype_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['contenttypes.ContentType'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('portfolio', ['MediaContentType'])

        # Changing field 'GalleryItem.content_type'
        db.alter_column('portfolio_galleryitem', 'content_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.MediaContentType']))


    def backwards(self, orm):
        
        # Deleting model 'MediaContentType'
        db.delete_table('portfolio_mediacontenttype')

        # Changing field 'GalleryItem.content_type'
        db.alter_column('portfolio_galleryitem', 'content_type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType']))


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'portfolio.gallery': {
            'Meta': {'ordering': "['position']", 'object_name': 'Gallery'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'portfolio.galleryitem': {
            'Meta': {'ordering': "['position']", 'object_name': 'GalleryItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.MediaContentType']"}),
            'context': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        'portfolio.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'portfolio.mediacontenttype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'MediaContentType', '_ormbases': ['contenttypes.ContentType']},
            'contenttype_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['contenttypes.ContentType']", 'unique': 'True', 'primary_key': 'True'})
        },
        'portfolio.video': {
            'Meta': {'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'portfolio.videoformat': {
            'Meta': {'ordering': "['position']", 'object_name': 'VideoFormat'},
            'format': ('django.db.models.fields.CharField', [], {'default': "'720p'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Video']"}),
            'video_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']
