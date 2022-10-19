#!/usr/bin/python3
"""

This module representes the program called console

"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


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

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_obj = eval(f"{args[0]}()")
            new_obj.save()
            print(f"{new_obj.id}")
        
    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            storage.reload()
            objects = storage.all()
            if (f"{args[0]}.{args[1]}") not in objects.keys():
                print("** no instance found **")
            else:
                print(objects[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            storage.reload()
            objects = storage.all()
            if (f"{args[0]}.{args[1]}") not in objects.keys():
                print("** no instance found **")
            else:
                del(objects[f"{args[0]}.{args[1]}"])
                storage.save()

    def do_all(self, arg):
        args = arg.split()
        if len(args) > 0 and args[0] != "BaseModel":
            print("** class doesn't exist **")
        storage.reload()
        objects = storage.all()
        for k in objects.keys():
            print(objects[k])
    
    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        else:
            storage.reload()
            objects = storage.all()
            if (f"{args[0]}.{args[1]}") not in objects.keys():
                print("** no instance found **")
            else:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    my_obj = objects[f"{args[0]}.{args[1]}"]
                    for k, v in list(my_obj.__dict__.items()):
                        my_obj.__dict__[args[2]] = args[3]
                    storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
