from socks.client import Client
from socks.server import Server

class Socks:
    """Class of methods to work with sockets from both server and client side"""

    def __init__(self) -> None:
        pass

    def server(self):
        return Server()

    def client(self):
        return Client()