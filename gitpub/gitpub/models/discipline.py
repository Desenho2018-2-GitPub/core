from django.db import models


class Discipline(models.Model):
    """
    A discipline is created by an user and belongs to a class
    """
    description = models.CharField(max_length=140)
    name = models.CharField(max_length=50)
