# Generated by Django 4.2.8 on 2024-01-13 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CairoCoinPlus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CairoCoinPlus.user'),
        ),
    ]