# Module: VIEW

# Classes
from app import Application
from console import Console

class View:

    def __init__(self) -> None:
        pass

    # Provides class "Console" and their methods to work with
    def console(self):
        return Console

    # Provides class "Application" and their methods to work with
    def app(self):
        return Application





