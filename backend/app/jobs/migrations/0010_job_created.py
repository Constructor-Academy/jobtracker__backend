# Generated by Django 3.0.2 on 2020-01-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_auto_20191218_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='created'),
        ),
    ]