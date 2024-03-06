import os
import string

directory = "alphabet_files"
os.makedirs(directory, exist_ok=True)

for letter in string.ascii_uppercase:
    with open(f"{directory}/{letter}.txt", "w") as file:
        file.write(f"This is the file for letter.{letter}\n")