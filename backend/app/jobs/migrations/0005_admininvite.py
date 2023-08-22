# Generated by Django 2.2.2 on 2019-12-16 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_initial'),
        ('jobs', '0004_auto_20191125_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254, verbose_name='user')),
                ('admin_email', models.EmailField(max_length=254, verbose_name='admin email')),
                ('status', models.CharField(choices=[('1', 'Admin invited to open account'), ('2', 'Admin existed and has been added as admin of requesting user.'), ('3', 'Admin account created and added as admin of requesting user.')], max_length=2, verbose_name='status')),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invites', to='emails.Email', verbose_name='sent invite')),
            ],
        ),
    ]
