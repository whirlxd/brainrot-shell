import os
def handle_rmdir(directory):
    try:
        os.rmdir(directory)
        print(f"Removed directory '{directory}'")
    except FileNotFoundError:
        print(f"rmdir: failed to remove '{directory}': No such file or directory")
    except OSError:
        print(f"rmdir: failed to remove '{directory}': Directory not empty")