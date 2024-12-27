# Generated by Django 5.1.4 on 2024-12-27 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('student_phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='groups.group')),
            ],
        ),
    ]