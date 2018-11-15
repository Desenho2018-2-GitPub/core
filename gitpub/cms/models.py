"""
Models module
"""
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Abstract class for RegisteredUser
    """
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class AnonymousUser(CustomUser):
    """
    AnonymousUser
    """
    def save(self, *args, **kwargs):
        self.pk = 0
        self.name = "Anonymous User"
        try:
            super(AnonymousUser, self).save(*args, **kwargs)
        except:
            AnonymousUser.objects.get(id=0)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=0, name="Anonymous User")
        return obj


class RegisteredUser(CustomUser):
    """
    Abstract class for Admin and Student
    """
    registry = models.IntegerField()
    username = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'registry']

class Material(models.Model):
    """
    Materials belong to projects
    """
    url = models.CharField(max_length=140)


class Period(models.Model):
    """
    A class belongs to a period (Semester 1 or 2)
    """
    SEMESTER_CHOICES = (
        (1, 'First'),
        (2, 'Second')
    )
    YEAR_CHOICES = [(r, r) for r in range(2000, datetime.date.today().year+1)]
    year = models.IntegerField(choices=YEAR_CHOICES)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)

    def __str__(self):
        return ", ".join([self.semester, self.year])


class Course(models.Model):
    """
    A course is created by an user and belongs to a class
    """
    description = models.CharField(max_length=140)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    """
    A classroom can be created and/or enrolled by an user
    and belongs to a course
    """
    name = models.CharField(max_length=50)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='classrooms'
    )
    owner = models.ForeignKey(
        RegisteredUser, 
        on_delete=models.CASCADE,
        related_name='owned_classrooms'
    )
    enrolled_users = models.ManyToManyField(
        RegisteredUser,
        related_name='enrolled_classrooms'
    )
    period = models.ForeignKey(
        Period,
        on_delete=models.CASCADE,
        related_name='classrooms'
    )

    def __str___(self):
        return self.name

    class Meta:
        ordering = ('course', 'period', 'name')


class Project(models.Model):
    """
    A project belongs to a classroom, has comments and material
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    views = models.IntegerField(default=0)
    classroom = models.ManyToManyField(
        Classroom,
        related_name='projects'
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    A comment is written by an user to a project.
    """
    text = models.CharField(max_length=140)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='comments'    
    )

    def __str__(self):
        return self.text
