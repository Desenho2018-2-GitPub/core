from django.db import models
from .user import User
from .project import Project


class Comment(models.Model):
    """
    A comment is written by an user to a project.
    """
    text = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
