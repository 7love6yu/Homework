str = input()
newstr = ""

for char in str:
    if char.isupper():
        char = chr((ord(char)-60) % 26 + ord('A'))
        newstr += char
    elif char.islower():
        char = chr((ord(char)-94) % 26 + ord('a'))
        newstr += char
    else:
        newstr += char

print(newstr)



