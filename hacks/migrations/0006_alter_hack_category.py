# hacks/migrations/0006_alter_hack_category.py
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('hacks', '0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hack',
            name='category',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to='categories.category',
                null=False,
            ),
        ),
    ]
