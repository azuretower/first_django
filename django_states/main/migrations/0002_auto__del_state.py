# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'State'
        db.delete_table(u'main_state')


    def backwards(self, orm):
        # Adding model 'State'
        db.create_table(u'main_state', (
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('capital', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('population', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'main', ['State'])


    models = {
        
    }

    complete_apps = ['main']