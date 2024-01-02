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

            print('Dicks Alive 1 ', self.host)

            client.connect(self.host)

            print('Dicks Alive 2')

            # Setup
            client.setblocking(0)

            print('Dicks Alive 3')
            
            # Create header
            header = f"{len(self.username):<{self.header_length}}".encode('UTF-8')

            print('header:', header)
            print('username:', self.username)

            print(header+self.username.encode('UTF-8'))

            # Send content
            client.send(header+self.username.encode('UTF-8'))
        
        except Exception as e:
            log.error('Error on Client.connect() : ', )
            return False
