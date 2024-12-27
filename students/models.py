from django.db import models
from groups.models import Group


class Student(models.Model):
    full_name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')
    date_of_birth = models.DateField()
    student_phone = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.full_name
