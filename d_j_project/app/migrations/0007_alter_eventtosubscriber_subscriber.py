# Generated by Django 3.2.4 on 2021-06-23 18:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_eventtosubscriber_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventtosubscriber',
            name='subscriber',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Подписчик'),
        ),
    ]
