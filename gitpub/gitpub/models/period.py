import datetime
from django.db import models

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
    YEAR_CHOICES = [(r, r) for r in range(2009, datetime.date.today().year+1)]
    year = models.IntegerField(choices=YEAR_CHOICES)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
