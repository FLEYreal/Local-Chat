
class ChatModel:
    def __init__(self):
        self.connected = False
        self.nickname = "Steve"

    def connect(self, network_name, password):
        pass

    def disconnect(self):
        self.conneced = False

    def send_message(self, message):
        pass

    def get_messages(self):
        return

    def set_name(self, new_nickname):
        self.nickname = new_nickname

    def close_network(self):
        pass

    def create_network(self):
        pass

    def connected(self):
        return self.conneced
