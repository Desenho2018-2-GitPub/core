from django.db import models
from .course import Course
from .user import User
from .period import Period


class Classroom(models.Model):
    """
    A classroom can be created and/or enrolled by an user
    and belongs to a course
    """
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    enrolled_user = models.ManyToManyField(User)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)

    def __str___(self):
        return self.name

    class Meta:
        ordering = ('course', 'period', 'name')
