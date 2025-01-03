from rest_framework import serializers
from apps.chats.models import DirectChat


class DirectChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectChat
        fields = (
            "id",
            "user1",
            "user2",
        )


__all__ = ("DirectChatCreateSerializer",)
