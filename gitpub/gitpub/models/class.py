from django.db import models


class Class(models.Model):
    """
    A class can be created and/or enrolled by an user and belongs to a discipline
    """
    name = models.CharField(max_length=50)
