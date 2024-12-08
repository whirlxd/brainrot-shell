import os
def handle_ls():
    for file in os.listdir():
        print(file)