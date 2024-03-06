import os

def check_path(path):
    if os.path.exists(path):
        directory_name = os.path.dirname(path)
        file_name = os.path.basename(path)
        return True, directory_name, file_name
    else:
        return False, None, None

path_to_check = '/your/specified/path'
exists, directory, file = check_path(path_to_check)

if exists:
    print("The path exists.")
    print(f"Directory:{directory}")
    print(f"Filename:{file}")
else:
    print("The path does not exist.")