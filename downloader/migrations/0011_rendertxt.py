# Generated by Django 3.1.1 on 2022-11-01 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0010_downloader_updatedon'),
    ]

    operations = [
        migrations.CreateModel(
            name='RenderTxt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Robots', models.FileField(blank=True, upload_to='uploads/robots/')),
                ('Ads', models.FileField(blank=True, upload_to='uploads/ads/')),
            ],
        ),
    ]
