# Generated by Django 2.2.4 on 2024-12-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0007_auto_20241230_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(max_length=2000),
        ),
    ]
