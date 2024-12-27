from django.db import models
from subjects.models import Subject


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher_phone = models.CharField(max_length=15)
    teacher_email = models.EmailField(max_length=100, unique=True)
    work_experience = models.PositiveIntegerField()
    image = models.ImageField()
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name='teachers')


    def __str__(self):
        return f"{self.first_name}{self.last_name}"