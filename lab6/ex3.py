#python ex3.py E:\IMR-models
import sys
import os


def ex3():
    try:
        directory_path = sys.argv[1]

        if not os.path.exists(directory_path):
            raise Exception(f"No {directory_path} path found!")

        total_size = 0
        os.chdir(directory_path)
        for root, dir, files in os.walk("."):
            for file in files:
                full_fileName = os.path.join(root, file)
                if os.path.isfile(file):
                    total_size += os.path.getsize(file)
                print(full_fileName)

        print(f"Total size is: {total_size} bytes")

    except Exception as e:
        print(e)


ex3()
