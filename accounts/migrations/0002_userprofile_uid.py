# Generated by Django 2.0.2 on 2018-02-25 13:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='uid',
            field=models.CharField(default='bfghjkl', max_length=8, unique=True),
            preserve_default=False,
        ),
    ]
