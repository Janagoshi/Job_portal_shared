# Generated by Django 4.0.4 on 2022-05-22 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobp', '0014_teacher_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
