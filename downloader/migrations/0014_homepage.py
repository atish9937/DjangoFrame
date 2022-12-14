# Generated by Django 3.1.1 on 2022-11-02 07:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0013_auto_20221101_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Home', max_length=60)),
                ('ShowAllDownloader', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=6)),
                ('Meta_Title', models.CharField(blank=True, max_length=80)),
                ('Meta_Description', models.CharField(blank=True, max_length=200)),
                ('Featured_Image', models.ImageField(blank=True, upload_to='uploads/featuredimages/')),
                ('Logo', models.ImageField(blank=True, upload_to='uploads/logos/')),
                ('Body_Title', models.CharField(blank=True, max_length=80)),
                ('Content_Above_DownloadersList', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('Content_Below_DownloadersList', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('Recently_Downloaded', models.TextField(blank=True)),
                ('Updatedon', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
