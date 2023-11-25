#python ex4.py E:\IMR-models
import os
import sys

def ex4():
    try:
        directory_path = sys.argv[1]

        if not os.path.exists(directory_path):
            raise Exception(f"No {directory_path} path found!")

        if not os.access(directory_path, os.R_OK):
            raise Exception(f"No read permissions for the directory '{directory_path}'.")

        all_files = os.listdir(directory_path)
        if len(all_files) == 0:
            raise Exception("Directory is empty!")

        dict = {}
        # print(all_files)
        for file in all_files:
            _, extension = os.path.splitext(file)
            if extension in dict.keys():
                dict[extension] += 1
            else:
                dict[extension] = 1

        for key in dict:
            print(f"Extension {key} appears {dict[key]} time(s).")

    except Exception as e:
        print(e)

ex4()