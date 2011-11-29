# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Project'
        db.delete_table('portfolio_project')

        # Deleting field 'Gallery.project'
        db.delete_column('portfolio_gallery', 'project_id')

        # Adding field 'Gallery.position'
        db.add_column('portfolio_gallery', 'position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2), keep_default=False)

        # Adding field 'GalleryItem.position'
        db.add_column('portfolio_galleryitem', 'position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Project'
        db.create_table('portfolio_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('portfolio', ['Project'])

        # Adding field 'Gallery.project'
        db.add_column('portfolio_gallery', 'project', self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['portfolio.Project']), keep_default=False)

        # Deleting field 'Gallery.position'
        db.delete_column('portfolio_gallery', 'position')

        # Deleting field 'GalleryItem.position'
        db.delete_column('portfolio_galleryitem', 'position')


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
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'context': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'portfolio.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'portfolio.video': {
            'Meta': {'object_name': 'Video'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'portfolio.videoformat': {
            'Meta': {'object_name': 'VideoFormat'},
            'format': ('django.db.models.fields.CharField', [], {'default': "'720p'", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'video': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Video']"}),
            'video_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['portfolio']
