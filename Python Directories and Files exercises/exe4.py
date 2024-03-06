def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

file_path = 'path_to_your_file.txt'
number_of_lines = count_lines(file_path)
print(number_of_lines, "The number of lines in the file: ")