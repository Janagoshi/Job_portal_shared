# Generated by Django 4.0.4 on 2022-05-01 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobp', '0004_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='language2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='level',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]