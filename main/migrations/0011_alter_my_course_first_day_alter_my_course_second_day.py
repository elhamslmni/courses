# Generated by Django 4.0.4 on 2022-08-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_my_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_course',
            name='first_day',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='my_course',
            name='second_day',
            field=models.CharField(max_length=30),
        ),
    ]
