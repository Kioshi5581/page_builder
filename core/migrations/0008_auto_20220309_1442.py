# Generated by Django 3.2.9 on 2022-03-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220309_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='pawnhost_section_h1',
            new_name='why_pawnhost_h1',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='pawnhost_section_image',
            new_name='why_pawnhost_image',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='pawnhost_section_p',
            new_name='why_pawnhost_p',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='pawnhost_section_title',
        ),
        migrations.AddField(
            model_name='homepage',
            name='why_pawnhost_title',
            field=models.CharField(default='YO', max_length=200),
            preserve_default=False,
        ),
    ]
