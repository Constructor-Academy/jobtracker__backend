# Generated by Django 3.0.2 on 2020-07-22 13:23

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='dev email')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('to', models.EmailField(max_length=254, verbose_name='To')),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
                ('compiled_template', models.TextField(blank=True, verbose_name='compiled_template')),
                ('bcc', models.TextField(blank=True, verbose_name='bcc')),
                ('is_sent', models.BooleanField(default=False, verbose_name='is_sent')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmailType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200, unique=True, verbose_name='email key')),
                ('subject', models.CharField(max_length=200, verbose_name='subject')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('template', models.TextField(verbose_name='template extension')),
            ],
        ),
    ]
