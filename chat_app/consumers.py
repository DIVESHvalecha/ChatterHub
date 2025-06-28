from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from collections import defaultdict
from .models import Group, Message

room_user_counts = defaultdict(int)
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connected")
        self.groupName = self.scope['url_route']['kwargs']['groupName']
        await self.channel_layer.group_add(self.groupName, self.channel_name)
        await self.accept()
        room_user_counts[self.groupName] += 1
        await self.channel_layer.group_send(
            self.groupName,
            {
                "type": "online.count",
                "room_count": room_user_counts[self.groupName]
            }
        )

    async def receive(self, text_data):
        print("Message received:", text_data)
        profile = await database_sync_to_async(lambda: self.scope["user"].profile)()
        await self.channel_layer.group_send(
            self.groupName,
            {
                "type": "chat.message",
                "message": text_data,
                "sender": profile.username,
                "profile_pic": (
                    profile.profile_picture.url 
                    if profile.profile_picture else "/media/default.jpeg"
                ),
            }
        )
        @database_sync_to_async
        def get_group(group_name):
            return Group.objects.filter(group_name=self.groupName).first()

        @database_sync_to_async
        def create_message(group, profile, text_data):
            return Message.objects.create(
                group=group,
                user=profile,
                message=text_data
            )
        group = await get_group(self.groupName)
        await create_message(group, profile, text_data)
        
    async def disconnect(self, close_code):
        print("WebSocket disconnected with code:", close_code)
        await self.channel_layer.group_discard("room", self.channel_name)
        room_user_counts[self.groupName] -= 1
        await self.channel_layer.group_send(
            self.groupName,
            {
                "type": "online.count",
                "room_count": room_user_counts[self.groupName]
            }
        )
        # await self.close()
        
    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({
            "type": "chat_message",
            "message": message,
            "sender": event["sender"],
            "profile_pic": event["profile_pic"],
        }))  
        # await self.send("message received thanks for sending")
        
    async def online_count(self, event):
        await self.send(text_data=json.dumps({
            "type": "online_count",
            "room_count": room_user_counts[self.groupName]
        }))