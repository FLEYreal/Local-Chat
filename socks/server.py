# Imports
import socket
from utils.display_logs import DisplayLogs
import select


# Setup
log = DisplayLogs()
log.__init__()


# Class
class Server:
    """Class of methods to work with sockets on server side"""

    username = ''
    host = ()
    header_length = 16
    sockets_list = []
    clients_dict = {}

    def __init__(
            self,
            username = "Guest",
            host = ('0.0.0.0', 5005),
            header_length = 16
    ) -> None:
        self.username = username
        self.host = host
        self.header_length = header_length

    def create(self, return_server: bool = False) -> None:
        """
            This method creates a socket, binds it to the host provided in "host" variable and starts listening to new connections with method "self.listen".

            Args:
                return_server (bool): By default it's false and it creates infinite loop to listen to connection by itself but turning it on, you can get "server" and provide your own functionality using it.

            Important to know:
                - This method creates infinite loop.
        """

        log.info('Creating server...')

        try:
            # Create Socket
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(self.host)

            # Launch socket
            server.listen()

            # Append server to the list
            self.sockets_list.append(server)

            # Loop to listen to connection
            if not return_server:
                self.listen(server)
            
            # Return server if you need to make your own functionality with it
            elif return_server:
                return server
        
        except Exception as e:
            log.error('Error on Server.create() : ', e)
            return False

    def delete_server(self) -> None:
        pass

    def receive(self, client: socket.socket) -> None:
        """Tries to receive sent to server content, it has to first send header and only after the data needed!

        Args:
            client (socket.socket): A server that message was sent to.

        Returns:
            dict: Returns received standartized object with header and data provided.
        """

        try:
            # Get header with everything needed
            header = client.recv(self.header_length)

            # If no header
            if not len(header):
                raise Exception('Feels like nothing was sent in the header!')
            
            # Get provided length
            length = int(header.decode('UTF-8').strip())

            # If all's good, return standartized object
            log.success('Received message from client!')
            return {
                'header': header,
                'data': client.recv(length)
            }
        
        except Exception as e:
            log.error('Error on Server.receive() : ', e)
            return False

    def listen(self, server: socket.socket) -> None:
        """
        Starts infinite loop to listen to new connections of clients on server provided as argument.

        Args:
            server (socket.socket): A server socket whose connection it'll listen to.
        """

        log.info("Listening to connections...")

        try:

            if server == False:
                raise Exception('Provided server equals "False" which most times implies that error happened on Server.create(). It also means that Server.listen() returns False as well!')

            while True:

                # Create waiting list
                rlist, _, xlist = select.select(self.sockets_list, [], self.sockets_list)

                # Parse ready list
                for _socket in rlist:

                    if _socket == server:

                        # Accept new client
                        client, address = server.accept()

                        # Receive user's data
                        data = self.receive(client)
                        if not data:
                            continue

                        # Save data
                        self.sockets_list.append(client)
                        self.clients_dict[client] = data
                        
                        # Print received data
                        log.info(data)

        except Exception as e:
            log.error('Error on Server.listen() : ', e)
            return False
