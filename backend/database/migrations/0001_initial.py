# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FCIGroup'
        db.create_table(u'database_fcigroup', (
            ('group', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'database', ['FCIGroup'])

        # Adding model 'FCIGroupSection'
        db.create_table(u'database_fcigroupsection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.FCIGroup'])),
            ('section', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'database', ['FCIGroupSection'])

        # Adding unique constraint on 'FCIGroupSection', fields ['group', 'section']
        db.create_unique(u'database_fcigroupsection', ['group_id', 'section'])

        # Adding model 'Family'
        db.create_table(u'database_family', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True)),
        ))
        db.send_create_signal(u'database', ['Family'])

        # Adding model 'Breed'
        db.create_table(u'database_breed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.FCIGroupSection'])),
            ('wikipedia', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'database', ['Breed'])

        # Adding M2M table for field related on 'Breed'
        m2m_table_name = db.shorten_name(u'database_breed_related')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_breed', models.ForeignKey(orm[u'database.breed'], null=False)),
            ('to_breed', models.ForeignKey(orm[u'database.breed'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_breed_id', 'to_breed_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'FCIGroupSection', fields ['group', 'section']
        db.delete_unique(u'database_fcigroupsection', ['group_id', 'section'])

        # Deleting model 'FCIGroup'
        db.delete_table(u'database_fcigroup')

        # Deleting model 'FCIGroupSection'
        db.delete_table(u'database_fcigroupsection')

        # Deleting model 'Family'
        db.delete_table(u'database_family')

        # Deleting model 'Breed'
        db.delete_table(u'database_breed')

        # Removing M2M table for field related on 'Breed'
        db.delete_table(db.shorten_name(u'database_breed_related'))


    models = {
        u'database.breed': {
            'Meta': {'object_name': 'Breed'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['database.FCIGroupSection']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_rel_+'", 'null': 'True', 'to': u"orm['database.Breed']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'}),
            'wikipedia': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'database.family': {
            'Meta': {'object_name': 'Family'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True'})
        },
        u'database.fcigroup': {
            'Meta': {'object_name': 'FCIGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'group': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'})
        },
        u'database.fcigroupsection': {
            'Meta': {'unique_together': "(('group', 'section'),)", 'object_name': 'FCIGroupSection'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['database.FCIGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['database']