# Generated by Django 4.2.13 on 2024-06-08 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datatable',
            old_name='line',
            new_name='line_no',
        ),
    ]
