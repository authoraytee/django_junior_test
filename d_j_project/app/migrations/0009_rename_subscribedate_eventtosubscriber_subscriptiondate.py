# Generated by Django 3.2.4 on 2021-06-24 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_eventtosubscriber_subscribedate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventtosubscriber',
            old_name='SubscribeDate',
            new_name='SubscriptionDate',
        ),
    ]
