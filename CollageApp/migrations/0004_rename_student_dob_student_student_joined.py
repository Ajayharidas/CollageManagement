# Generated by Django 4.0.3 on 2022-04-12 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CollageApp', '0003_course_course_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_dob',
            new_name='student_joined',
        ),
    ]