#!/usr/bin/python3
"""

This module representes the program called console

"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class defines the console wich is the
    command interpreter for the airbnb clone
    """
    prompt = '(hbnb)'
    file = None

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        self.close()
        return True

    def do_EOF(self, arg):
        """End of File"""
        self.close()
        return True

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
