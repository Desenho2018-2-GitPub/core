"""
Models module
"""
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from notifyr.agents import observer, observed
from notifyr.functions import target
from cms.utils.email import EmailSender
from markdownx.models import MarkdownxField
import os


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
        self.name = "Usuário Anônimo"
        try:
            super(AnonymousUser, self).save(*args, **kwargs)
        except BaseException:
            AnonymousUser.objects.get(id=0)

    def delete(self):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=0, name="Anonymous User")
        return obj

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@observer('send_email')
class RegisteredUser(CustomUser):
    """
    Abstract class for Admin and Student
    """
    registry = models.IntegerField()
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    bio = models.CharField(max_length=280, default="")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'registry']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def send_email(self, *args, **kwargs):
        should_send_email = os.getenv('SHOULD_SEND_EMAIL', False)

        if should_send_email:
            project = args[0]
            email_body = "Olá, {0}!\n\nUm usuário adicionou um novo projeto à disciplina {1}, turma {2}. \
            \nVerifique a plataforma GitPub para mais informações".format(
                self.name, project.classroom.all().last().course.name, project.classroom.all().last().name, )

            sender = EmailSender()
            sender.send_email(self.email, email_body)
        else:
            print(
                "An email would notify {0} about the new project.".format(
                    self.name))


class Period(models.Model):
    """
    A class belongs to a period (Semester 1 or 2)
    """
    SEMESTER_CHOICES = (
        (1, 'First'),
        (2, 'Second')
    )
    YEAR_CHOICES = [(r, r)
                    for r in range(2000, datetime.date.today().year + 1)]
    year = models.IntegerField(choices=YEAR_CHOICES)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)

    def __str__(self):
        return ", ".join([self.semester, self.year])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    """
    A course is created by an user and belongs to a class
    """
    description = models.CharField(max_length=140)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def number_of_classrooms(self):
        return len(self.classrooms.all())

    number_of_classrooms = property(number_of_classrooms)

    def number_of_projects(self):
        classrooms = self.classrooms.all()
        total = 0

        for classroom in classrooms:
            total += classroom.number_of_projects

        return total

    number_of_projects = property(number_of_projects)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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

    def number_of_projects(self):
        return len(self.projects.all())

    number_of_projects = property(number_of_projects)

    class Meta:
        ordering = ('course', 'period', 'name')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@observed
class Project(models.Model):
    """
    A project belongs to a classroom, has comments and material
    """
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=280)
    description = models.CharField(max_length=10000)
    views = models.IntegerField(default=0)
    classroom = models.ManyToManyField(
        Classroom,
        related_name='projects'
    )

    def __str__(self):
        return self.name

    @target
    def save(self, *args, **kwargs):
        print("Saving instance of project")
        super(Project, self).save(*args, **kwargs)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    """
    A comment is written by an user to a project.
    """
    text = models.CharField(max_length=500)
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Material(models.Model):
    """
    Materials belong to projects
    """
    url = models.CharField(max_length=1000)

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='materials'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MyModel(models.Model):
    myfield = MarkdownxField()
