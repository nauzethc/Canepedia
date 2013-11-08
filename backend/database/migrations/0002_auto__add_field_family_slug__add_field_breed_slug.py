# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Family.slug'
        db.add_column(u'database_family', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'Breed.slug'
        db.add_column(u'database_breed', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Family.slug'
        db.delete_column(u'database_family', 'slug')

        # Deleting field 'Breed.slug'
        db.delete_column(u'database_breed', 'slug')


    models = {
        u'database.breed': {
            'Meta': {'object_name': 'Breed'},
            'family': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Family']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_rel_+'", 'to': u"orm['database.Breed']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'}),
            'wikipedia': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'database.family': {
            'Meta': {'object_name': 'Family'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['database']