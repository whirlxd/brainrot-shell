import shlex
def handle_cat(file_paths):
    file_paths = shlex.split(file_paths)
    contents = []
    for file_path in file_paths:
        try:
            with open(file_path, "r") as file:
                contents.append(file.read().strip())
        except FileNotFoundError:
            print(f"{file_path}: No such file or directory")
            return
    print(" ".join(contents))