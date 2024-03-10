#!/usr/bin/python3
"""
This module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter.

    Attributes:
        prompt (str): The command prompt
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF signal to exit the program

        Usage: Ctrl + D
        """
        print()
        return True

    def emptyline(self):
        """
        Does nothing when an empty line is entered
        """
        pass

    def help_quit(self):
        """
        Help documentation for the quit command
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Help documentation for the EOF command
        """
        print("EOF signal to exit the program")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
