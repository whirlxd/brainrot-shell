#!/usr/bin/env python3
import sys
import shlex
from commands.help import handle_help
from commands.ls import handle_ls
from commands.mkdir import handle_mkdir
from commands.exit import handle_exit
from commands.echo import handle_echo
from commands.rmdir import handle_rmdir
from commands.cat import handle_cat
from commands.pwd import handle_pwd
from commands.cd import handle_cd
from commands.touch import handle_touch
from commands.type import handle_type
from commands.path import handle_path
def main():
    while True:
        sys.stdout.write("@brainrot: ")
        sys.stdout.flush()
        user_command = input()
        if user_command == "map":
            handle_ls()
        elif user_command.startswith("touch "):
            handle_touch(user_command[6:])
        elif user_command.startswith("spawn "):
            handle_mkdir(user_command[6:])
        elif user_command.startswith("despawn "):
            handle_rmdir(user_command[8:])
        elif user_command.startswith("ragequit"):
            handle_exit()
        elif user_command == "help":
            handle_help()
        elif user_command.startswith("yap "):
            handle_echo(user_command[4:])
        elif user_command.startswith("loot "):
            handle_cat(user_command[5:])
        elif user_command == "pwd":
            handle_pwd()
        elif user_command.startswith("hawktuah "):
            handle_cd(user_command[9:])
        elif user_command.startswith("typeshi "):
            handle_type(user_command[8:])
        else:
            command_parts = shlex.split(user_command)
            handle_path(command_parts)
        sys.stdout.flush()
if __name__ == "__main__":
    main()