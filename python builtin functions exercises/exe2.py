def letters_c(text):
    upper_case = sum(1 for char in text if char.isupper())
    lower_case = sum(1 for char in text if char.islower())
    
    return upper_case, lower_case

text = str(input("Текст еңгіз: "))
upper, lower = letters_c(text)
print(upper, "Uppercase letters ")
print(lower, "Lowercase letters ")