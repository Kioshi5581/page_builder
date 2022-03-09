# Generated by Django 3.2.9 on 2022-03-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20220309_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('page_title', models.CharField(max_length=200)),
                ('page_keywords', models.CharField(max_length=500)),
                ('page_desc', models.TextField()),
                ('hero_h1', models.CharField(max_length=200)),
                ('hero_h2', models.CharField(max_length=200)),
                ('hero_p', models.TextField()),
                ('servers_title', models.CharField(max_length=200)),
                ('payments_options', models.CharField(max_length=500)),
                ('hero_title', models.CharField(max_length=200)),
                ('table_title', models.CharField(max_length=200)),
                ('table_title2', models.CharField(max_length=200)),
                ('table_title3', models.CharField(max_length=200)),
                ('table_title4', models.CharField(max_length=200)),
            ],
        ),
    ]
