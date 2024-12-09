def handle_touch(file_path):
    try:
        with open(file_path, "r"):
            print(f"{file_path}: File already exists")
            return
    except FileNotFoundError:
        pass
    
    with open(file_path, "w"):
        pass
    print(f"Created file {file_path}")