# Imports
from colorama import just_fix_windows_console
from termcolor import colored

# Class
class DisplayLogs():
    """
    A class for displaying standardized logs in the console with predefined types like INFO, WARNING, ERROR, SUCCESS.

    Requires the colorama and termcolor libraries for proper functionality.
    """

    def __init__(self) -> None:
        """Initialize the DisplayLogs class."""
        just_fix_windows_console()

    def message(self, msg, color = "cyan", type = "INFO", is_print = True) -> str:
        """
        Display a standardized message with optional console printing.

        Args:
            msg (str): The main message to display.
            color (str): The color of the log type.
            type (str): The name of the type, displayed in square brackets before the message.
            is_print (bool): Should the message be printed in the console automatically?

        Returns:
            str: The converted, standardized message for logging in both console and log files.

        Example:
            display = DisplayLogs()
            log_msg = display.message("This is an example message", color="blue", type="CUSTOM", is_print=True)
        """

        # Convert message
        tag = colored(type, color)
        result = f"[ {tag} ] {msg}"

        # Print message if needed
        if is_print:
            print(result)

        return result

    def info(self, msg = "<Info Message Undefined>", is_print = True) -> str:
        """
        Displays info log
        
        Args:
            msg (str) : Main message to display.
            is_print (bool) : Is there a need to print it in console automatically?

        Returns:
            str: Converted, standartized message for logging in both console and log files.
        """
        return self.message(msg=msg, is_print=is_print)
    
    def warn(self, msg = "<Warning Message Undefined>", is_print = True) -> str:
        """
        Displays warning log
        
        Args:
            msg (str) : Main message to display.
            is_print (bool) : Is there a need to print it in console automatically?

        Returns:
            str: Converted, standartized message for logging in both console and log files.
        """
        return self.message(msg, "yellow", "WARN", is_print)
    
    def error(self, msg = "<Error Message Undefined>", is_print = True) -> str:
        """
        Displays error log
        
        Args:
            msg (str) : Main message to display.
            is_print (bool) : Is there a need to print it in console automatically?

        Returns:
            str: Converted, standartized message for logging in both console and log files.
        """
        return self.message(msg, "red", "ERROR", is_print)
    
    def success(self, msg = "<Success Message Undefined>", is_print = True) -> str:
        """
        Displays successful log
        
        Args:
            msg (str) : Main message to display.
            is_print (bool) : Is there a need to print it in console automatically?

        Returns:
            str: Converted, standartized message for logging in both console and log files.
        """
        return self.message(msg, "green", "SUCCESS", is_print)