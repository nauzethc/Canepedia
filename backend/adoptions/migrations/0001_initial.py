# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dog'
        db.create_table(u'adoptions_dog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('crossbreed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'adoptions', ['Dog'])

        # Adding M2M table for field breed on 'Dog'
        m2m_table_name = db.shorten_name(u'adoptions_dog_breed')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dog', models.ForeignKey(orm[u'adoptions.dog'], null=False)),
            ('breed', models.ForeignKey(orm[u'database.breed'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dog_id', 'breed_id'])

        # Adding M2M table for field related on 'Dog'
        m2m_table_name = db.shorten_name(u'adoptions_dog_related')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_dog', models.ForeignKey(orm[u'adoptions.dog'], null=False)),
            ('to_dog', models.ForeignKey(orm[u'adoptions.dog'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_dog_id', 'to_dog_id'])

        # Adding model 'Brood'
        db.create_table(u'adoptions_brood', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crossbreed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('birth', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal(u'adoptions', ['Brood'])

        # Adding M2M table for field breed on 'Brood'
        m2m_table_name = db.shorten_name(u'adoptions_brood_breed')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('brood', models.ForeignKey(orm[u'adoptions.brood'], null=False)),
            ('breed', models.ForeignKey(orm[u'database.breed'], null=False))
        ))
        db.create_unique(m2m_table_name, ['brood_id', 'breed_id'])

        # Adding M2M table for field related on 'Brood'
        m2m_table_name = db.shorten_name(u'adoptions_brood_related')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('brood', models.ForeignKey(orm[u'adoptions.brood'], null=False)),
            ('dog', models.ForeignKey(orm[u'adoptions.dog'], null=False))
        ))
        db.create_unique(m2m_table_name, ['brood_id', 'dog_id'])


    def backwards(self, orm):
        # Deleting model 'Dog'
        db.delete_table(u'adoptions_dog')

        # Removing M2M table for field breed on 'Dog'
        db.delete_table(db.shorten_name(u'adoptions_dog_breed'))

        # Removing M2M table for field related on 'Dog'
        db.delete_table(db.shorten_name(u'adoptions_dog_related'))

        # Deleting model 'Brood'
        db.delete_table(u'adoptions_brood')

        # Removing M2M table for field breed on 'Brood'
        db.delete_table(db.shorten_name(u'adoptions_brood_breed'))

        # Removing M2M table for field related on 'Brood'
        db.delete_table(db.shorten_name(u'adoptions_brood_related'))


    models = {
        u'adoptions.brood': {
            'Meta': {'object_name': 'Brood'},
            'birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'breed': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Breed']", 'symmetrical': 'False'}),
            'crossbreed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['adoptions.Dog']", 'symmetrical': 'False'})
        },
        u'adoptions.dog': {
            'Meta': {'object_name': 'Dog'},
            'birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'breed': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Breed']", 'symmetrical': 'False'}),
            'crossbreed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'related': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_rel_+'", 'to': u"orm['adoptions.Dog']"})
        },
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

    complete_apps = ['adoptions']