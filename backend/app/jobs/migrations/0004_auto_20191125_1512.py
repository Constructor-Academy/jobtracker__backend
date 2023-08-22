# Generated by Django 2.2.2 on 2019-11-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20191115_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('WH', 'Wishlist'), ('AP', 'Applied'), ('IN', 'Interviewing'), ('OF', 'Offered'), ('AC', 'Accepted'), ('RJ', 'Rejected')], default='WH', max_length=2, verbose_name='status'),
        ),
    ]
