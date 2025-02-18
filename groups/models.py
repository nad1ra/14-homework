from django.db import models
from django.shortcuts import reverse

from students.models import Student
from subjects.base_models import BaseModel
from teachers.models import Teacher

class Group(BaseModel):
    group_name = models.CharField(max_length=50)
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, related_name='group')
    students = models.ManyToManyField(Student, related_name='groups')

    def __str__(self):
        return self.group_name


    def get_detail_url(self):
        return reverse('groups:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('groups:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('groups:update', args=[self.pk])
