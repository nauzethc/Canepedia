# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Family'
        db.create_table(u'database_family', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'database', ['Family'])

        # Adding model 'Breed'
        db.create_table(u'database_breed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('wikipedia', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'database', ['Breed'])

        # Adding M2M table for field family on 'Breed'
        m2m_table_name = db.shorten_name(u'database_breed_family')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('breed', models.ForeignKey(orm[u'database.breed'], null=False)),
            ('family', models.ForeignKey(orm[u'database.family'], null=False))
        ))
        db.create_unique(m2m_table_name, ['breed_id', 'family_id'])

        # Adding M2M table for field related on 'Breed'
        m2m_table_name = db.shorten_name(u'database_breed_related')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_breed', models.ForeignKey(orm[u'database.breed'], null=False)),
            ('to_breed', models.ForeignKey(orm[u'database.breed'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_breed_id', 'to_breed_id'])


    def backwards(self, orm):
        # Deleting model 'Family'
        db.delete_table(u'database_family')

        # Deleting model 'Breed'
        db.delete_table(u'database_breed')

        # Removing M2M table for field family on 'Breed'
        db.delete_table(db.shorten_name(u'database_breed_family'))

        # Removing M2M table for field related on 'Breed'
        db.delete_table(db.shorten_name(u'database_breed_related'))


    models = {
        u'database.breed': {
            'Meta': {'object_name': 'Breed'},
            'family': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Family']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_rel_+'", 'to': u"orm['database.Breed']"}),
            'wikipedia': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'database.family': {
            'Meta': {'object_name': 'Family'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['database']