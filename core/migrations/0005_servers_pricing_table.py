# Generated by Django 4.0.3 on 2022-03-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_homepage_feature_section_card_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='pricing_table',
            field=models.ManyToManyField(to='core.pricing_table'),
        ),
    ]
