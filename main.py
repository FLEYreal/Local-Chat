# Imports
from socks import Server, Client
from utils.display_logs import DisplayLogs

# Logging
log = DisplayLogs()
log.launch()

# Data
username = input('What\'s your username? : ')
is_host = input('Be a host of the chat / Connect to existing chat ? (1 / 2) : ')

if is_host == "1":
    server = Server(
        username=username
    )
    server.create()

if is_host == "2":

    ip = input('What\'s IP? : ')
    port = input('What\'s Port? : ')

    client = Client(
        username=username,
        host=(ip, int(port))
    )

    client.connect()