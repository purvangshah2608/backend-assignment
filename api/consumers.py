from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    active_connections = set()

    async def connect(self):
        """Called when a WebSocket connection is established."""
        await self.accept()
        self.active_connections.add(self)  # Store the connection

    async def disconnect(self, close_code):
        """Called when the WebSocket disconnects."""
        self.active_connections.remove(self)

    async def receive(self, text_data):
        """Called when a message is received."""
        # Broadcast the raw text message to all connected clients
        for connection in self.active_connections:
            await connection.send(text_data=text_data)
