# Generated by Django 3.1.1 on 2022-11-01 15:21

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0003_pages_pageid'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloader',
            name='Content_Above_InputField',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AddField(
            model_name='downloader',
            name='Content_Below_InputField',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]