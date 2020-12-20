from django.db import models


class Translation(models.Model):
    word = models.CharField(max_length=250)
