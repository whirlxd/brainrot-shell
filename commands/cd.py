import os
def handle_cd(directory):
    if directory == "~":
        os.chdir(os.path.expanduser("~"))
    else:
        try:
            os.chdir(directory)
        except FileNotFoundError:
            print(f"cd: {directory}: No such file or directory")