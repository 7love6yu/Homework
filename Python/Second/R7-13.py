str = input()
count = 0

for char in str:
    if char.isalpha():
        count += 1
    elif char.isdigit():
        count += 1
        
print(count)