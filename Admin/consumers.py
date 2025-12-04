import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DriverConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("drivers", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("drivers", self.channel_name)

    # client tomondan status update kelganda
    async def receive(self, text_data):
        data = json.loads(text_data)
        event_type = data.get("type")
        print('############', data, '############')

        if event_type == "status_change":
            await self.channel_layer.group_send(
                "drivers",
                {
                    "type": "driver_status_changed",
                    "driver_id": data["driver_id"],
                    "status": data["status"],
                }
            )
        elif event_type == "location_update":
            await self.channel_layer.group_send(
                "drivers",
                {
                    "type": "driver_location_updated",
                    "driver_id": data["driver_id"],
                    "lat": data["lat"],
                    "lng": data["lng"]
                }
            )

    # WebSocket orqali groupga yuborish
    async def driver_status_changed(self, event):
        await self.send(text_data=json.dumps(event))

    async def driver_location_updated(self, event):
        await self.send(text_data=json.dumps(event))


class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("orders", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("orders", self.channel_name)

    async def send_order_update(self, order_id, status, driver_id=None):
        await self.channel_layer.group_send(
            "orders",
            {
                "type": "order_update",
                "order_id": order_id,
                "status": status,
                "driver_id": driver_id
            }
        )

    async def order_update(self, event):
        await self.send(text_data=json.dumps(event))

