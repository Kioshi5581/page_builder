# Generated by Django 4.0.3 on 2022-03-15 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='feature_section_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.call_to_action'),
        ),
    ]
