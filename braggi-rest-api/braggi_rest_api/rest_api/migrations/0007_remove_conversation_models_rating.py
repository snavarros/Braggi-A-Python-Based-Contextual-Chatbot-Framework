# Generated by Django 2.0.6 on 2018-07-15 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0006_auto_20180715_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation_models',
            name='rating',
        ),
    ]