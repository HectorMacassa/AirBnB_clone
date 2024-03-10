#!/usr/bin/python3
"""
This module
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Entry point of the command interpreter.

    Attributes:
        prompt (str): The command prompt
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

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

    def do_create(self, arg):
        """
        Creates a new instance of a class

        Usage: create <class name>
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance

        Usage: show <class name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id

        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()


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
