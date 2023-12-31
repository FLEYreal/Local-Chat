# Imports
import socket
from utils.display_logs import DisplayLogs

# Setup
log = DisplayLogs()
log.__init__()

# Class
class Server:
    """Class of methods to work with sockets on server side"""

    username = ''
    host = ()

    def __init__(
            self, 
            username="Guest", 
            host = ('localhost', 5005)
    ) -> None:
        self.username = username
        self.host = host

    def create_server(self) -> None:
        
        # Create Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(self.host)

        # Launch socket
        s.listen()

        # Loop to listen to connection
        self.listen_connections()

    def delete_server(self) -> None:
        pass

    def receive(self) -> None:
        pass

    def listen_connections(self) -> None:
        
        log.info("Listening to connections")