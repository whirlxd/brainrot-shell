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
        sys.stdout.write("$ ")
        sys.stdout.flush()
        user_command = input()
        if user_command == "ls":
            handle_ls()
        elif user_command.startswith("touch "):
            handle_touch(user_command[6:])
        elif user_command.startswith("mkdir "):
            handle_mkdir(user_command[6:])
        elif user_command.startswith("rmdir "):
            handle_rmdir(user_command[6:])
        elif user_command.startswith("ragequit"):
            handle_exit()
        elif user_command == "help":
            handle_help()
        elif user_command.startswith("yap "):
            handle_echo(user_command[4:])
        elif user_command.startswith("cat "):
            handle_cat(user_command[4:])
        elif user_command == "pwd":
            handle_pwd()
        elif user_command.startswith("cd "):
            handle_cd(user_command[3:])
        elif user_command.startswith("type "):
            handle_type(user_command[5:])
        else:
            command_parts = shlex.split(user_command)
            handle_path(command_parts)
        sys.stdout.flush()
if __name__ == "__main__":
    main()