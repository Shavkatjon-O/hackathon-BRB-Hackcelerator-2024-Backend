# Generated by Django 5.0.7 on 2024-09-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_remove_chat_is_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='is_group',
            field=models.BooleanField(default=False),
        ),
    ]
