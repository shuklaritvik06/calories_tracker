# Generated by Django 4.2.2 on 2023-06-18 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CalorieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField(blank=True)),
                ('time', models.TimeField(auto_now=True)),
                ('date', models.DateField(auto_now=True)),
                ('total_calories', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('met_expectations', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
