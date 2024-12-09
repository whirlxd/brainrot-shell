import os
import subprocess

def handle_path(command_parts):
    command_name = command_parts[0]
    command_args = command_parts[1:]

    found = False
    for directory in os.environ.get("PATH").split(os.pathsep):
        executable_path = os.path.join(directory, command_name)
        if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
            found = True
            break

    if found:
        try:
            subprocess.run([command_name] + command_args, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
    else:
        print(f"{command_name}: command not found")