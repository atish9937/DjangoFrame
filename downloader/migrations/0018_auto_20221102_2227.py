# Generated by Django 3.1.1 on 2022-11-02 16:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0017_auto_20221102_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headercode',
            name='Header_Codes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='rendertxt',
            name='Ads',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
