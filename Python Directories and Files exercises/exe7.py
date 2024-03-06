def copy_file(source_path, destination_path):

    with open(source_path, 'r') as source_file, open(destination_path, 'w') as destination_file:
        
        content = source_file.read()
        
        destination_file.write(content)