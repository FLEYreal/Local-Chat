# Imports
import socket
from colorama import Fore
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
    client = False

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

            # Assign client globally
            self.client = client

            # Setup message field so to send messages
            self.message_field()
        
        except Exception as e:
            log.error(f'Error on Client.connect() : {e}')
            return False
        
    def send_message(self, message):

        try:
            if not self.client:
                raise Exception("Client is not assigned, first use Client.connect() to setup connection")
            
            if not message:
                raise Exception("No message provided")
            
            # Data to send to the server
            data = {
                "type": "send", # Types: "Join" | "Send" | "Leave"
                "username": self.username,
                "message": message
            }

            # Create header
            header = f"{len(str(data)):<{self.header_length}}".encode('UTF-8')

            # Send content
            self.client.send(header+str(data).encode('UTF-8'))

            # If everything worked well
            return True
        
        except Exception as e:
            log.error(f'on Client.send_message() : {e}')
            return False


    def message_field(self):

        try:
            if not self.client:
                raise Exception("Client is not assigned, first use Client.connect() to setup connection")

            while True:

                # Field to type your message
                message = input(f"{self.username} {Fore.BLACK}>>> {Fore.RESET}")

                # Send message and get boolean saying either it's succeed
                is_send = self.send_message(message)

                # If message is sent, display it
                if is_send:
                    print(f'{self.username} {Fore.CYAN}(You) {Fore.BLACK}:{Fore.RESET} {message}')
        
        except Exception as e:
            log.error(f'Error on Client.message_field() : {e}')
            return False
