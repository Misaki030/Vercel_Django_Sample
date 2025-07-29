from django.db import models

class SampleModel(models.Model):
    code = models.IntegerField()
    msg = models.CharField(max_length=100)