# Generated by Django 3.0.2 on 2020-01-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200, verbose_name='notification key')),
                ('subject', models.CharField(max_length=200, verbose_name='subject')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('template', models.TextField(verbose_name='template extension')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribed_notification_types', models.ManyToManyField(blank=True, related_name='subscribed_user_notification_profiles', to='notifications.NotificationType', verbose_name='subscribed notification types')),
            ],
        ),
    ]
