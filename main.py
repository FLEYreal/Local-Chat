# Imports
from socks import Server, Client
from utils.display_logs import DisplayLogs
from colorama import Fore

# Logging
log = DisplayLogs()
log.launch()

# Data
username = input(f'{Fore.CYAN}What\'s your username? {Fore.BLACK}>>>{Fore.RESET} ').strip()
is_host = input(f'{Fore.CYAN}Be a host of the chat / Connect to existing chat ? (1 / 2) {Fore.BLACK}>>>{Fore.RESET} ').strip()

if is_host == "1":
    server = Server(
        username=username
    )
    server.create()

if is_host == "2":

    ip = input(f'{Fore.CYAN}What\'s host IP? {Fore.BLACK}>>>{Fore.RESET} ')

    client = Client(
        username=username,
        host=(ip, 5005)
    )

    client.connect()