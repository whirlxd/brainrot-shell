import os
import subprocess
PATH = os.environ.get("PATH").split(os.pathsep)

def handle_path(command_parts):
    command_name = command_parts[0]
    command_args = command_parts[1:]

    found = False
    for directory in PATH:
        executable_path = os.path.join(directory, command_name)
        if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
            subprocess.run([executable_path] + command_args)
            found = True
            break
    if not found:
        print(f"{command_name}: command not found")