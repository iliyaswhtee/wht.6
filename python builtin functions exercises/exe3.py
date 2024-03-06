def palindrome(s):
    return s == s[::-1]

s = str(input("Сөз енгізіңіз: "))
ans = palindrome(s)

if ans:
    print("Ия")
else:
    print("Жоқ")