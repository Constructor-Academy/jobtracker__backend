# Generated by Django 3.0.2 on 2023-03-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculums', '0003_auto_20201019_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.CharField(blank=True, max_length=400, verbose_name='education description'),
        ),
    ]
