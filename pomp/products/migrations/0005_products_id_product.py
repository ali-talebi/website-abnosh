# Generated by Django 4.2.1 on 2023-05-20 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_size_length_alter_products_size_width_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Id_product',
            field=models.IntegerField(blank=True, null=True, verbose_name='بارکد یا کد محصول '),
        ),
    ]