from ast import keyword
from pyexpat import model
from django.db import models

class webSite(models.Model):
    keywords = models.CharField(max_length=200, default="")
    site = models.CharField(max_length=200, default="detikcom")
    fromDate = models.DateField()
    toDate = models.DateField()
    page = models.IntegerField()

    def __str__(self):
        return self.keywords