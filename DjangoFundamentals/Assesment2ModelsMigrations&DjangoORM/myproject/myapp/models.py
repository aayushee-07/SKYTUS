
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return self.name
