from django.db import models


class User(models.Model):
    """
    A user can be a student, professor, guest or a admin
    """
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
