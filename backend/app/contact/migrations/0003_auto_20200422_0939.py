# Generated by Django 3.0.2 on 2020-04-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200422_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='name'),
        ),
    ]
