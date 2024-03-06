import os

def check_access(path):
    access_rights = {
        'Exists': os.path.exists(path),
        'Readable': os.access(path, os.R_OK),
        'Writable': os.access(path, os.W_OK),
        'Executable': os.access(path, os.X_OK)
    }
    return access_rights

path_to_check = '/your/specified/path'
access = check_access(path_to_check)

print(f"Access rights for {path_to_check}:")
print(f"Exists: {access['Exists']}")
print(f"Readable: {access['Readable']}")
print(f"Writable: {access['Writable']}")
print(f"Executable: {access['Executable']}")