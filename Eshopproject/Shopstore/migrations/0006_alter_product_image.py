# Generated by Django 4.1.5 on 2023-04-05 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopstore', '0005_remove_product_photo_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='ssdd', upload_to='product'),
            preserve_default=False,
        ),
    ]
