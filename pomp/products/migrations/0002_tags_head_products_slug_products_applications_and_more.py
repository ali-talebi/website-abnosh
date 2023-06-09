# Generated by Django 4.2.1 on 2023-05-20 21:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام کلمه کلیدی')),
            ],
            options={
                'verbose_name_plural': 'کلمات کلیدی',
                'db_table': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='head_products',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='آدرس'),
        ),
        migrations.AddField(
            model_name='products',
            name='applications',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='کاربرد ها محصول'),
        ),
        migrations.AddField(
            model_name='products',
            name='descriptions',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='توضیحات محصول '),
        ),
        migrations.AddField(
            model_name='products',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='Products_Image', verbose_name='عکس محصول'),
        ),
        migrations.AddField(
            model_name='products',
            name='status',
            field=models.CharField(blank=True, choices=[('d', 'پیش نویس'), ('p', 'منتشر')], default='p', max_length=1, null=True, verbose_name='وضعیت'),
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='products.tags', verbose_name='کلمات کلیدی'),
        ),
    ]
