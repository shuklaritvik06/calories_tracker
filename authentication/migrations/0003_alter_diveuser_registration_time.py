# Generated by Django 4.2.2 on 2023-06-17 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_diveuser_registration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diveuser',
            name='registration_time',
            field=models.TimeField(default=datetime.time(16, 26, 0, 900919)),
        ),
    ]
