# Generated by Django 4.2.2 on 2023-06-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_diveuser_registration_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diveuser',
            name='registration_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='diveuser',
            name='registration_time',
            field=models.TimeField(),
        ),
    ]
