# Generated by Django 4.0.6 on 2022-08-03 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_remove_course_idcourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='state',
        ),
    ]