# Generated by Django 5.0.7 on 2024-09-05 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_chat_image_chat_is_group_alter_chat_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='is_group',
        ),
    ]