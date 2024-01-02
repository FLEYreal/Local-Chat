# Imports
import socket
from utils.display_logs import DisplayLogs


# Setup
log = DisplayLogs()
log.__init__()


# Class
class Client:
    """Class of methods to work with sockets on client side"""

    username = ''
    header_length = 16
    host = ()

    def __init__(
            self,
            username = "Guest",
            header_length = 16,
            host = ('localhost', 5005),
    ) -> None:
        self.username = username
        self.header_length = header_length
        self.host = host

    def connect(self):

        log.info('Trying to connect to server...')

        try:

            # Create client
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(self.host)

            # Setup
            client.setblocking(0)

            # Data to send to the server
            data = {
                "type": "join", # Types: "Join" | "Send" | "Leave"
                "username": self.username,
                "message": f"{self.username} has entered the chat."
            }
            
            # Create header
            header = f"{len(str(data)):<{self.header_length}}".encode('UTF-8')

            # Send content
            client.send(header+str(data).encode('UTF-8'))
        
        except Exception as e:
            log.error('Error on Client.connect() : ', )
            return False
