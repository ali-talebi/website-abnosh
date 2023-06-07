# Generated by Django 4.2.1 on 2023-05-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_team_member_linkedin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=300, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=200, verbose_name='موضوع')),
                ('message', models.TextField(verbose_name='متن پیام ')),
            ],
            options={
                'verbose_name_plural': 'ارتباط با ما ',
                'db_table': 'Contact_us',
            },
        ),
    ]
