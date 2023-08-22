# Generated by Django 3.0.2 on 2020-10-16 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='uuid')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='uuid')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('institution', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('description', models.CharField(blank=True, max_length=400)),
                ('link', models.URLField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='curriculums.Category')),
            ],
        ),
    ]