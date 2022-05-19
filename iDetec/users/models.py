from django.db import models
import os
# Create your models here.
class User(models.Model):
    id = models.IntegerField
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

class Images(models.Model):
    id = models.IntegerField
    chemin = models.ImageField(upload_to="imageAno", null=True, blank=True)

class Anomaly(models.Model):
    id = models.IntegerField
    nom = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)

class Pixel(models.Model):
    id = models.IntegerField
    x = models.FloatField(null=False)
    y = models.FloatField(null=False)
    anomaly = models.ForeignKey(Anomaly, on_delete=models.CASCADE)

