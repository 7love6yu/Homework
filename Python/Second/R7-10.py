n = input()
n = int(n)
result = []
for i in range(1,n+1):
    if n % i == 0:
        result.append(i)

print(result)
    