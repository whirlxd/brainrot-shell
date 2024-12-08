import os
valid_commands = ["ragequit", "touch","yap", "type", "path", "pwd", "cd", "cat", "help" , "ls"]
PATH = os.environ.get("PATH").split(os.pathsep)
def handle_type(type_command):
    if type_command in valid_commands:
        print(f"{type_command} is a shell builtin")
        return
    found = False
    for directory in PATH:
        executable_path = os.path.join(directory, type_command)
        if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
            print(f"{type_command} is {executable_path}")
            found = True
            break
    if not found:
        print(f"{type_command}: not found")