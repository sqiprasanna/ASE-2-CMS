# Generated by Django 2.1.2 on 2018-12-09 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0004_auto_20181209_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='querytoadmin',
            old_name='admin',
            new_name='query',
        ),
    ]
