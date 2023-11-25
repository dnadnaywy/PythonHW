#python ex2.py E:\pycharmProjectsUAIC\pythonLabs\lab6-ex

import sys
import os


def ex2():
    try:
        directory_path = sys.argv[1]

        if not os.path.exists(directory_path):
            raise Exception(f"No {directory_path} path found!")

        matching_files = []

        os.chdir(directory_path)

        files = os.listdir()

        i = 1
        for file in files:
            _, extension = os.path.splitext(file)
            new_name = "file" + str(i) + extension
            i += 1
            if new_name in files:
                raise Exception("There is already a file with that name!")
            os.rename(file, new_name)
            matching_files.append(new_name)

        print(matching_files)
        if len(matching_files) == 0:
            print("No found files with given extension!")
    except Exception as e:
        print(e)
    except FileNotFoundError as e:
        print(f"Error: {e}")


ex2()
