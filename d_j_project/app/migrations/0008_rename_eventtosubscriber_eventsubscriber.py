# Generated by Django 3.2.4 on 2021-06-22 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210622_0914'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventToSubscriber',
            new_name='EventSubscriber',
        ),
    ]