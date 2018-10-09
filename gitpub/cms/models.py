from django.db import models
import datetime

class User(models.Model):
    """
    A user can be a student, professor, guest or a admin
    """
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.username

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    """
    A classroom can be created and/or enrolled by an user
    and belongs to a course
    """
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_user')
    enrolled_user = models.ManyToManyField(User)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
