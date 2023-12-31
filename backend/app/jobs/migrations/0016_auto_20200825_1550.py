# Generated by Django 3.0.2 on 2020-08-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_auto_20200304_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_city',
            field=models.CharField(blank=True, max_length=50, verbose_name='company city'),
        ),
        migrations.AddField(
            model_name='job',
            name='company_country',
            field=models.CharField(blank=True, max_length=50, verbose_name='company country'),
        ),
        migrations.AddField(
            model_name='job',
            name='company_street',
            field=models.CharField(blank=True, max_length=50, verbose_name='company street'),
        ),
        migrations.AddField(
            model_name='job',
            name='company_zip',
            field=models.CharField(blank=True, max_length=8, verbose_name='company zip'),
        ),
        migrations.AddField(
            model_name='job',
            name='contact',
            field=models.TextField(blank=True, max_length=50, verbose_name='company contact'),
        ),
        migrations.AddField(
            model_name='job',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=50, verbose_name='company contact email'),
        ),
        migrations.AddField(
            model_name='job',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=16, verbose_name='company contact phone'),
        ),
        migrations.AddField(
            model_name='job',
            name='contact_title',
            field=models.CharField(blank=True, max_length=50, verbose_name='company contact title'),
        ),
        migrations.AlterField(
            model_name='job',
            name='notes',
            field=models.TextField(blank=True, max_length=50, verbose_name='notes'),
        ),
    ]
