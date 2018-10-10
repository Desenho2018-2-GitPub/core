"""
Models module
"""
import datetime
from django.db import models

class CustomUser(models.Model):
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
            AnonymousUser.objects.get(id=1)

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
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=80)
    token = models.CharField(max_length=150)

    def create_project(self):
        pass


class Student(RegisteredUser):
    """
    Student
    """
    pass


class Admin(RegisteredUser):
    """
    Admins make other users admins
    """
    def make_admin(self, CustomUser):
        pass

    def create_discipline(self):
        pass


class Material(models.Model):
    """
    Materials belong to projects
    """
    url = models.CharField(max_length=140)


class Period(models.Model):
    """
    A class belongs to a period (Semester 1 or 2)
    """
    FIRST = 1
    SECOND = 2
    SEMESTER_CHOICES = (
        (FIRST, 'First'),
        (SECOND, 'Second')
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    """
    A classroom can be created and/or enrolled by an user
    and belongs to a course
    """
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                              related_name='owner_user')
    enrolled_user = models.ManyToManyField(CustomUser)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)

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
    classroom = models.ManyToManyField(Classroom)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """
    A comment is written by an user to a project.
    """
    text = models.CharField(max_length=140)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
