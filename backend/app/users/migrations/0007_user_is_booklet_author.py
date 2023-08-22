# Generated by Django 3.0.2 on 2021-04-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_final_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_booklet_author',
            field=models.BooleanField(default=False, help_text='Permission needed to generate student booklets', verbose_name='is booklet author'),
        ),
    ]
