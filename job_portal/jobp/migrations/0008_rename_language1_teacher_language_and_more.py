# Generated by Django 4.0.4 on 2022-05-01 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobp', '0007_alter_teacher_language2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='language1',
            new_name='language',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='language2',
        ),
    ]
