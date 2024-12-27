# Generated by Django 5.1.4 on 2024-12-27 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50)),
                ('class_teacher', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group', to='teachers.teacher')),
            ],
        ),
    ]
