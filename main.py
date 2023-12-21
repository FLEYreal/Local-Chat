# Libs
import json

# Classes
from model import Model
from view import View
from controller import Controller

# Main function to launch entire app
def main():

    with open('config.json', 'r') as file:
        config = json.load(file)

    controller = Controller( 
        name=config['default_name']
    )

    controller.setup_chat()

    pass


# If this file is main, then launch app
if __name__ == "__main__":
    main()