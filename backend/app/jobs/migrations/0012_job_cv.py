# Generated by Django 3.0.2 on 2020-02-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20200129_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='cv',
            field=models.FileField(blank=True, upload_to='cvs/', verbose_name='cv'),
        ),
    ]
