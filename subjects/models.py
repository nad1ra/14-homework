from django.db import models
from django.shortcuts import reverse
from .base_models import BaseModel


class Subject(BaseModel):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

    def get_teacher_count(self):
        return self.teachers.count()

    def get_detail_url(self):
        return reverse('subjects:detail', args=[self.pk])

    def get_delete_url(self):
        return reverse('subjects:delete', args=[self.pk])

    def get_update_url(self):
        return reverse('subjects:update', args=[self.pk])

