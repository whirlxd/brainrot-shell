import os
def handle_showgyatt():
    files_with_sizes = [(file, os.path.getsize(file)) for file in os.listdir() if os.path.isfile(file)]
    files_with_sizes.sort(key=lambda x: x[1], reverse=True)
    for file, size in files_with_sizes:
        size_in_mb = size / (1024 * 1024)
        print(f"{file}: {size_in_mb:.2f} MB ({size} bytes)")

