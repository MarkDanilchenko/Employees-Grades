# Generated by Django 4.2.7 on 2023-11-14 16:46

import Entry_task__main.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Grade title', max_length=50, unique=True, verbose_name='Grade')),
            ],
            options={
                'verbose_name_plural': 'Grades',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First name', max_length=50, validators=[Entry_task__main.models.employeeName_validator], verbose_name='First name')),
                ('last_name', models.CharField(help_text='Last name', max_length=50, validators=[Entry_task__main.models.employeeName_validator], verbose_name='Last name')),
                ('second_name', models.CharField(blank=True, default='-', help_text='Second name', max_length=50, null=True, validators=[Entry_task__main.models.employeeName_validator], verbose_name='Second name')),
                ('date_of_employment', models.DateField(default=datetime.datetime.today, help_text='Date of employment', verbose_name='Date of employment')),
                ('grade', models.ForeignKey(default='Not defined', help_text='Grade', on_delete=django.db.models.deletion.SET_DEFAULT, to='Entry_task__main.grade', verbose_name='Grade')),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
