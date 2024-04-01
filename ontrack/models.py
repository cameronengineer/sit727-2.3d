from django.db import models


class Unit(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    period = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Submission(models.Model):

    LEVELS = (
        ('a', 'Pass'),
        ('b', 'Credit'),
        ('c', 'Distinction'),
        ('d', 'High Distinction'),
    )

    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=30, choices=LEVELS)

    def __str__(self):
        return self.name