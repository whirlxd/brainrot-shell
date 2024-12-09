#!/usr/bin/env python3
import sys
import shlex
# from colorama import init, Back, Fore, Style
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
from commands.ksi import handle_ksi
from commands.thickofit import handle_thickofit
from commands.showgyatt import handle_showgyatt
from commands.fanum import handle_fanum
from commands.unalive import handle_unalive

def main():
    # init(autoreset=True)
    # sys.stdout.write(Back.GREEN + Fore.WHITE)
    while True:
        sys.stdout.write("@brainrot ~$: ")
        sys.stdout.flush()
        user_command = input()
        if user_command.startswith("map"):
            handle_ls()
        elif user_command.startswith("wipeout"):
            sys.stdout.write("\033[H\033[J")
        elif user_command.startswith("unalive "):
            handle_unalive(user_command[8:])
        elif user_command.startswith("fanum"):
            handle_fanum()
        elif user_command.startswith("showgyatt"):
            handle_showgyatt()
        elif user_command.startswith('thickofit'):
            handle_thickofit()   
        elif user_command.startswith("touch "):
            handle_touch(user_command[6:])
        elif user_command.startswith("ksi "):
            handle_ksi(user_command[4:])
        elif user_command.startswith("spawn "):
            handle_mkdir(user_command[6:])
        elif user_command.startswith("despawn "):
            handle_rmdir(user_command[8:])
        elif user_command.startswith("ragequit"):
            handle_exit()
        elif user_command.startswith("help"):
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