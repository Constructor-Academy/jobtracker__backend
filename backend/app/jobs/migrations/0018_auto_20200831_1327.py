# Generated by Django 3.0.2 on 2020-08-31 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_auto_20200831_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(choices=[('Finance', 'Finance'), ('Information Technology', 'Information Technology'), ('Education and Training', 'Education'), ('Business Administration', 'Business'), ('Marketing and Sales', 'Marketing'), ('Health Science', 'Health'), ('Technology', 'Technology'), ('Others', 'Others')], default='Others', max_length=100, verbose_name='categories'),
        ),
    ]
