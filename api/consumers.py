import asyncio
# from django.contrib.auth import get_user_model
# from channels.consumer import AsyncConsumer
# from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import PriceInMinutes














class PriceConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    # print('asjfkdhjbakjb')
    self.groupname='prices'
    await self.channel_layer.group_add(
      self.groupname,
      self.channel_name,
    )
    await self.accept()
    # print("connected------>", event)
    # await self.send({
    #     "type": "websocket.accept"
    #   })

    # price_object = await self.get_price()
    # print(price_object)
    # await self.send({
    #     "type": "websocket.send",
    #     "text": "hello world"
    #   })
  async def disconnect(self, close_code):
    # print("connected------>", event)
    # await self.disconnect()

    pass

  async def receive(self, text_data):
    data_point = json.loads(text_data)

    await self.channel_layer.group_send(
        self.groupname,
        {
          "type": "deprocessing",
          "value": data_point['value']
        }
      )

    print(">>>>>", text_data)
    pass


  async def deprocessing(self, event):
    value = event['value']
    await self.send(text_data=json.dumps({'value': value}))

    # print("connected------>", event)
    # await self.send({
    #     "type": "websocket.send",
    #     "text": value
    #   })


  # @database_sync_to_async
  # def get_price(self):
  #   return PriceInMinutes.objects.latest('timestamp')
