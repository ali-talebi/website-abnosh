# Generated by Django 4.2.1 on 2023-05-21 14:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_products_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='تاریخ'),
        ),
    ]
