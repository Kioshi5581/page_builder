# Generated by Django 3.2.9 on 2022-03-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_servers'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='feature_section_btn_href',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servers',
            name='feature_section_desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servers',
            name='feature_section_img',
            field=models.ImageField(default='', upload_to='feature_section'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servers',
            name='feature_section_title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
