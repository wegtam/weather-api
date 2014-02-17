# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = []

    operations = [
        migrations.CreateModel(
            name = 'Country',
            options = {},
            fields = [('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),), ('country', models.CharField(verbose_name='Country', max_length=100),)],
            bases = (models.Model,),
        ),
        migrations.CreateModel(
            name = 'Weatherstation',
            options = {'verbose_name': 'Weatherstation', 'verbose_name_plural': 'Weatherstations'},
            fields = [('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),), ('name', models.CharField(verbose_name='Name', max_length=100),)],
            bases = (models.Model,),
        ),
        migrations.CreateModel(
            name = 'City',
            options = {},
            fields = [('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),), ('city', models.CharField(verbose_name='City', max_length=100),)],
            bases = (models.Model,),
        ),
        migrations.CreateModel(
            name = 'Weatherdata',
            options = {'verbose_name': 'Weather Data', 'verbose_name_plural': 'Weather Data`s'},
            fields = [('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False),), ('temperature', models.DecimalField(verbose_name='Temperature', max_digits=5, decimal_places=2),), ('humidity', models.DecimalField(verbose_name='Humidity', max_digits=6, decimal_places=2),), ('air_pressure', models.DecimalField(verbose_name='Air pressure', max_digits=7, decimal_places=3),), ('lightness', models.DecimalField(verbose_name='Lightness', max_digits=6, decimal_places=2),), ('altitude', models.DecimalField(verbose_name='Altitude', max_digits=7, decimal_places=3),), ('timestamp', models.DateTimeField(verbose_name='Timestamp', editable=False),), ('weatherstation', models.ForeignKey(to='api.Weatherstation', to_field='id'),), ('city', models.ForeignKey(to='api.City', verbose_name='City', to_field='id'),), ('country', models.ForeignKey(to='api.Country', verbose_name='Country', to_field='id'),)],
            bases = (models.Model,),
        ),
    ]
