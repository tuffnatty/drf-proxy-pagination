from django.db import models


class TestModel(models.Model):
    n = models.IntegerField("An integer")
    created = models.DateTimeField("ordering field", auto_now_add=True)
