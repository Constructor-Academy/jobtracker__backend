# Generated by Django 3.0.2 on 2020-01-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtype',
            name='key',
            field=models.CharField(max_length=200, unique=True, verbose_name='email key'),
        ),
    ]