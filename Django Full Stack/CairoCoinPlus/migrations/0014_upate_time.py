# Generated by Django 4.2.8 on 2024-02-14 06:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CairoCoinPlus', '0013_apiuser_history_day_token_limit'),
    ]

    operations = [
        migrations.CreateModel(
            name='upate_time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]