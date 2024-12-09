import os
def handle_cd(directory):
    if directory == "~":
        os.chdir(os.path.expanduser("~"))
        print(f"Back to home at {os.path.expanduser('~')}")
    else:
        try:
            os.chdir(directory)
            print(f"Changed directory to {directory}")
        except FileNotFoundError:
            print(f"hawktuah: {directory}: No such file or directory")