# Generated by Django 3.0.2 on 2020-11-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0018_auto_20200831_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='notes',
            field=models.TextField(blank=True, verbose_name='notes'),
        ),
    ]
