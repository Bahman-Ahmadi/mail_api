from channels.generic.websocket import WebsocketConsumer

class AppConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data="Welcome!")

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
    	url = text_data
    	print(url)
