# Generated by Django 3.2.8 on 2021-10-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=None, null=True),
        ),
    ]
