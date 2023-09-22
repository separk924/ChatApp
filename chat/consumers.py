import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    
    # connects and accepts chat connection
    # @param self: the consumer
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
    # @param self: the consumer
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )
    
    # This function is triggered when we send data from the WebSocket
    # @param self: the consumer
    # @param text_data: the message data that contains the message & username of sender
    #   in JSON format
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        # message that is received is spread to other instances, awaiting on 
        # the 'send' event
        await self.channel_layer.group_send(
            self.roomGroupName, 
            {
                "type": "sendMessage",
                "message": message,
                "username": username,
            }
        )
        
    # send the message
    # @param event: holds the data which was sent via th group_send() method of 
    #   the receive() function
    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        # send the message and username param to all instances that are active in 
        # the group
        await self.send(text_data = json.dumps({"message": message, "username": username}))