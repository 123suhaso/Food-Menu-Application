# Generated by Django 2.2.4 on 2024-12-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(max_length=2000),
        ),
    ]
