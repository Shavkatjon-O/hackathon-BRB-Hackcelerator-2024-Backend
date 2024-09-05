from rest_framework.generics import ListAPIView
from .serializers import MessageListSerializer
from apps.chats.models import Message


class MessageListView(ListAPIView):
    serializer_class = MessageListSerializer

    def get_queryset(self):
        return Message.objects.filter(chat=self.kwargs["chat_id"])

    def get_object(self):
        return self.request.user


__all__ = ("MessageListView",)
