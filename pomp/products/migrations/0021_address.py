# Generated by Django 4.2.1 on 2023-06-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_rename_email_newsletter_email_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500, verbose_name='آدرس ما ')),
                ('phone1', models.IntegerField(verbose_name='شماره تلفن 1 ')),
                ('phone2', models.IntegerField(verbose_name='شماره تلفن 2 ')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
            ],
            options={
                'verbose_name_plural': 'آدرس ما ',
                'db_table': 'Address',
            },
        ),
    ]