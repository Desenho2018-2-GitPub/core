from django.db import models


class Material(models.Model):
    """
    Materials belong to projects
    """
    url = models.CharField(max_length=140)
