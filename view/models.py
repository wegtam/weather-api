from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.


class Weatherstation(models.Model):
    name = models.CharField(u'Name', max_length=100)
    user = models.ForeignKey(User, verbose_name=u'User')

    class Meta:
        verbose_name = u'Weatherstation'
        verbose_name_plural = u'Weatherstations'

    def __str__(self):
        return self.name


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

