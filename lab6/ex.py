#python ex.py E:\pycharmProjectsUAIC\pythonLabs\lab5 .py
import sys
import os

def read_and_print_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Contents of file '{file_path}':\n{content}\n")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}\n")

def ex1():
    try:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]

        if not os.path.exists(directory_path):
            raise Exception(f"No {directory_path} path found!")

        if not file_extension.startswith("."):
            raise Exception(f"Invalid file extension!")

        matching_files = []

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(file_extension.lower()):
                    # If yes, add the file's absolute path to the list
                    matching_files.append(os.path.join(root, file))
                    read_and_print_file_contents(os.path.join(root, file))

        print(matching_files)
        if len(matching_files) == 0:
            print("No found files with given extension!")
    except Exception as e:
        print(e)

ex1()