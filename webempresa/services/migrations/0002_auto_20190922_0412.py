# Generated by Django 2.1.1 on 2019-09-22 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='services',
            new_name='Service',
        ),
    ]
