# Generated by Django 4.2.3 on 2025-03-03 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacks', '0003_hack_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hack',
            name='category',
        ),
    ]
