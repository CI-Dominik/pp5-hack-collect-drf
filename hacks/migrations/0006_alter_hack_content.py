# Generated by Django 4.2.3 on 2025-04-21 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacks', '0005_hack_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hack',
            name='content',
            field=models.TextField(max_length=255),
        ),
    ]
