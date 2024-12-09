import shutil

def handle_unalive(directory):
    try:
        shutil.rmtree(directory)
        print(f"Successfully removed '{directory}' and its contents.")
    except FileNotFoundError:
        print(f"unalive: failed to remove '{directory}': No such file or directory")
    except PermissionError:
        print(f"unalive: failed to remove '{directory}': Permission denied")
    except Exception as e:
        print(f"unalive: failed to remove '{directory}': {e}")

