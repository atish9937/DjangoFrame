# Generated by Django 3.1.1 on 2022-11-01 17:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0011_rendertxt'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Header_Codes', ckeditor.fields.RichTextField(blank=True)),
            ],
        ),
    ]
