from django.db import models
from django.shortcuts import reverse

from subjects.base_models import BaseModel


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(BaseModel):
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    student_phone = models.CharField(max_length=15)
    address = models.TextField()
    photo = models.ImageField(upload_to='students/')



    def __str__(self):
        return self.full_name

    def get_detail_url(self):
        return reverse('students:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('students:update', args=[self.pk])