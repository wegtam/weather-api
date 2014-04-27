from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Countries(models.Model):
    country = models.CharField(u'Land', max_length=100)
    isocode = models.CharField(u'ISOCODE', max_length=2)

    class Meta:
        verbose_name = u'Country'
        verbose_name_plural = u'Countries'

    def __str__(self):
        return self.country


class Cities(models.Model):
    city = models.CharField(u'Stadt', max_length=100)
    country = models.ForeignKey(Countries, verbose_name=u'Country')

    class Meta:
        verbose_name = u'City'
        verbose_name_plural = u'Cities'

    def __str__(self):
        return self.city


class Weatherstation(models.Model):
    name = models.CharField(u'Name', max_length=100)
    user = models.ForeignKey(User, verbose_name=u'User')
    city = models.ForeignKey(Cities, verbose_name=u'Stadt')

    class Meta:
        verbose_name = u'Weatherstation'
        verbose_name_plural = u'Weatherstations'

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('view-detail', [str(self.id)])


class Weatherdata(models.Model):
    temperature = models.DecimalField(u'Temperature', max_digits=5, decimal_places=2)
    humidity = models.DecimalField(u'Humidity', max_digits=6, decimal_places=2)
    air_pressure = models.DecimalField(u'Air pressure', max_digits=7, decimal_places=3)
    lightness = models.DecimalField(u'Lightness', max_digits=6, decimal_places=2)
    altitude = models.DecimalField(u'Altitude', max_digits=7, decimal_places=3)
    timestamp = models.DateTimeField(u'Timestamp', editable=False)
    weatherstation = models.ForeignKey(Weatherstation)
    user = models.ForeignKey(User, verbose_name=u'User')

    class Meta:
        verbose_name = u'Weather Data'
        verbose_name_plural = u'Weather Data`s'

    def __str__(self):
        name = self.weatherstation
        return str(name)

    def save(self, *args, **kwargs):
        self.timestamp = now()
        super(Weatherdata, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('view-detail', [str(self.weatherstation_id)])

    @models.permalink
    def get_absolute_url2(self):
        return ('view-user_ws', [str(self.user_id)])

