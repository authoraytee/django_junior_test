# Generated by Django 3.2.4 on 2021-06-23 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210623_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='subscriber',
        ),
        migrations.RemoveField(
            model_name='eventtosubscriber',
            name='subscriber',
        ),
    ]
