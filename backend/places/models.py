from django.db import models


class User (models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, default="no_name")


class Place (models.Model):
    place_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class Rate (models.Model):
    rate_id = models.AutoField(primary_key=True)
    rate = models.IntegerField()
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    placeHasRate = models.ManyToManyField(Place)
