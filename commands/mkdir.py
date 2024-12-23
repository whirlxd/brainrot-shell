import os
def handle_mkdir(directory):
    try:
        os.mkdir(directory)
        print(f"Created directory '{directory}'")
    except FileExistsError:
        print(f"mkdir: cannot create directory '{directory}': File exists")