# Generated by Django 3.0.2 on 2022-12-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20221121_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='job_search_area',
            field=models.CharField(default='Flexible', max_length=50, verbose_name='job search area'),
        ),
    ]
