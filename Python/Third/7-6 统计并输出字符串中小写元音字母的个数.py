str = input()
yuan = ['a','e','i','o','u']
cnt = 0

for char in str:
    if char in yuan:
        cnt +=1

print(cnt)
