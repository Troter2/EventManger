# Generated by Django 5.0.3 on 2024-03-24 14:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Club', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='club/'),
            preserve_default=False,
        ),
    ]
