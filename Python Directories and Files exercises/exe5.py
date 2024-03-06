def write_list_to_file(file_path, list_to_write):
    with open(file_path, 'w') as file:
        for item in list_to_write:
            file.write(f"{item}\n")

my_list = ['apple', 'banana', 'cherry']
file_path = 'path_to_your_file.txt'
write_list_to_file(file_path, my_list)
print(file_path, "List has been written to this file")