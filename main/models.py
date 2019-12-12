from django.db import models
import datetime
from django.utils import timezone

class Asutus(models.Model):
  nimi = models.CharField(max_length = 255)
  avamise_kellaaeg = models.TimeField(default=datetime.time(8, 30))
  sulgemise_kellaaeg = models.TimeField(default=datetime.time(19, 30))

class Tootaja(models.Model):
  asutus = models.ForeignKey(Asutus, on_delete=models.CASCADE)
  eesNimi = models.CharField(max_length = 120)
  perekonnaNimi = models.CharField(max_length = 120)

class TooajaTabel(models.Model):
  tootaja = models.ForeignKey(Tootaja, on_delete=models.CASCADE)
  kuupaev = models.DateField(default=timezone.now)
  tootunde = models.IntegerField(default=0)

