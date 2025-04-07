# hacks/migrations/0007_alter_hack_category_on_delete_cascade.py
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('hacks', '0006_alter_hack_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hack',
            name='category',
            field=models.ForeignKey(
                on_delete=models.CASCADE,
                to='categories.category',
                null=False,
            ),
        ),
    ]
