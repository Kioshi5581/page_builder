# Generated by Django 3.2.9 on 2022-03-09 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_homepage_href_btn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='about_p2',
        ),
    ]