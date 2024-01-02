# Imports
from socks import Socks
from utils.display_logs import DisplayLogs

# Logging
log = DisplayLogs()
log.launch()

# Experimenting
server = Socks().server()
server.create()
