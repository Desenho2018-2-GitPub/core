from django.db import models


class Project(models.Model):
    """
    A project belongs to a class, has comments and a material
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    views = models.IntegerField(default=0)
