from django.db import models
from django.shortcuts import reverse

from subjects.base_models import BaseModel
from subjects.models import Subject


class Teacher(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher_phone = models.CharField(max_length=15)
    teacher_email = models.EmailField(max_length=100, unique=True)
    work_experience = models.PositiveIntegerField()
    image = models.ImageField(upload_to='teachers/')
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, related_name='teachers')


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def get_detail_url(self):
        return reverse('teachers:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('teachers:update', args=[self.pk])
