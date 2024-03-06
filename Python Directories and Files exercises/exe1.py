import os

def list_directories(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def list_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def list_all(path):
    return os.listdir(path)

path_to_list = '/your/specified/path'

print("Directories:")
print(list_directories(path_to_list))

print("\nFiles:")
print(list_files(path_to_list))

print("\nAll directories and files:")
print(list_all(path_to_list))