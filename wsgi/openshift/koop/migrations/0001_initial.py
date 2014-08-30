# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Folder'
        db.create_table('koop_folder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, default='/')),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='children', default=None, to=orm['koop.Folder'])),
        ))
        db.send_create_signal('koop', ['Folder'])

        # Adding model 'Report'
        db.create_table('koop_report', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('folder', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='reports', default=None, to=orm['koop.Folder'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('koop', ['Report'])


    def backwards(self, orm):
        # Deleting model 'Folder'
        db.delete_table('koop_folder')

        # Deleting model 'Report'
        db.delete_table('koop_report')


    models = {
        'koop.folder': {
            'Meta': {'object_name': 'Folder'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'default': "'/'"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'children'", 'default': 'None', 'to': "orm['koop.Folder']"})
        },
        'koop.report': {
            'Meta': {'object_name': 'Report'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'reports'", 'default': 'None', 'to': "orm['koop.Folder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['koop']