# Module: MODEL

# Classes
from model.commands import Commands
from logs import Logs
from socket import Socks

class Model:

    def __init__(self) -> None:
        pass

    # Provides class "Commands" and their methods to work with
    def commands(self):
        return Commands
    
    # Provides class "Logs" and their methods to work with
    def logs(self):
        return Logs
    
    # Provides class "Socks" and their methods to work with
    # (aka class "Sockets" to avoid naming conflicts)
    def socks(self):
        return Socks