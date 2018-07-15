# Generated by Django 2.0.6 on 2018-07-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_conversation_models_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conversation_models',
            options={'ordering': ('created',)},
        ),
        migrations.RenameField(
            model_name='conversation_models',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='conversation_models',
            name='braggi_out',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='conversation_models',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='conversation_models',
            name='user_in',
            field=models.TextField(),
        ),
    ]
