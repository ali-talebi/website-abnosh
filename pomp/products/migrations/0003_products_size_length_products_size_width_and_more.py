# Generated by Django 4.2.1 on 2023-05-20 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_tags_head_products_slug_products_applications_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='size_length',
            field=models.FloatField(blank=True, null=True, verbose_name='سایز طول محصول'),
        ),
        migrations.AddField(
            model_name='products',
            name='size_width',
            field=models.FloatField(blank=True, null=True, verbose_name='سایز عرض محصول'),
        ),
        migrations.AddField(
            model_name='products',
            name='weigth',
            field=models.FloatField(blank=True, null=True, verbose_name='وزن محصول'),
        ),
    ]