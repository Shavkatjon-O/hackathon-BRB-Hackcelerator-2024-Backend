# import json
# from channels.generic.websocket import AsyncWebsocketConsumer


# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
#         self.room_group_name = f"chat_{self.chat_id}"

#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)

#         await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         sender = text_data_json["sender"]

#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {"type": "chat_message", "message": message, "sender": sender},
#         )

#     async def chat_message(self, event):
#         message = event["message"]
#         sender = event["sender"]

#         await self.send(text_data=json.dumps({"message": message, "sender": sender}))
# consumers.py
from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]

        self.send(text_data=json.dumps({"message": message}))
