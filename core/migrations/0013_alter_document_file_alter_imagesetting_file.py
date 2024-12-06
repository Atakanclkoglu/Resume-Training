# Generated by Django 5.1.2 on 2024-12-06 18:30

import Course_Django_Project.custom_storages
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_generalsetting_parameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, default='', storage=Course_Django_Project.custom_storages.DocumentStorage(), upload_to='', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='imagesetting',
            name='file',
            field=models.FileField(blank=True, null=True, storage=Course_Django_Project.custom_storages.ImageSettingStorage(), upload_to='', verbose_name='Image'),
        ),
    ]