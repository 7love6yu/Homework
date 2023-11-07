import random

x = int(input())
n = int(input())
m = int(input())

random.seed(x)
charList = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65,91)] + [str(i) for i in range(10)]

for _ in range(n):
    result = ''.join(random.choice(charList) for _ in range(m))
    print(result)