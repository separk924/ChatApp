import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    
    # connects and accepts chat connection
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            # creates group name for chatroom and adds group to the channel
            # layer group
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()
    
    # disconnects self from chat
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )
    
    # receive messages
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": username,
            }
        )
        
    # send messages
    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(text_date = json.dumps({"message": message, "username": username}))