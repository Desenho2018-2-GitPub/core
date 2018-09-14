from django.db import models
from .classroom import Classroom


class Project(models.Model):
    """
    A project belongs to a classroom, has comments and material
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    views = models.IntegerField(default=0)
    classroom = models.ManyToManyField(Classroom)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('classroom',)
