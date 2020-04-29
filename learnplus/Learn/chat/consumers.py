# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
# from channels.generic.websocket import AsyncWebsocketConsumer
import json
from . import models
from django.contrib.auth.models import User

class ChatConsumer(WebsocketConsumer):


    def fetch_messages(self, data):
        # messages = Message.last_10_messages()
        salon = data['salon']
        messages = Message.objects.filter(salon__nom=salon).order_by('date_add').all()[:20]
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)
    

    def new_message(self, data):
        auteur = data['from']
        salon = data['salon']
        salon_object = Salon.objects.get(nom=salon)
        auteur_user = User.objects.filter(username=auteur)[0]
        message = Message.objects.create(
            auteur=auteur_user,
            salon=salon_object,
            message=data['message']
        )
        content = {
            'command': 'new_message', 
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        print(messages)
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result
    
    def message_to_json(self, message):
        try:
            image = message.auteur.student_user.image.url
        except:
            image = message.auteur.instructor.image.url
        return {
            'auteur' : message.auteur.username,
            'auteur_image' : image,
            'message' : message.message,
            'date_add' : str(message.date_add)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message' : new_message,
        
    }
    # async def connect(self):
    def connect(self):
        self.salon = self.scope['url_route']['kwargs']['salon']
        self.room_group_name = 'chat_%s' % self.salon

        # Join room group
        # await self.channel_layer.group_add(
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )


    def send_message(self, message):
        self.send(text_data=json.dumps(message))
    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))


