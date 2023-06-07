# Generated by Django 4.2.1 on 2023-05-24 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_products_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='type_product',
            field=models.CharField(blank=True, choices=[('tableau', 'تابلو'), ('Pomp', 'پمپ')], max_length=20, null=True, verbose_name='نوع محصول '),
        ),
    ]
