# Generated by Django 2.2.4 on 2024-12-30 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0005_auto_20241230_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.URLField(max_length=10000),
        ),
    ]
