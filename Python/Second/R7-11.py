def isprime(number):
    if number <= 1:
        return  False
    if number == 2 :
        return  True
    if number % 2 == 0:
        return  False
    if number >= 3:
        for i in range(3,int(number**0.5)+1,2):
            if number % i == 0:
                return False

    return  True
a,b = input().split()
a = int(a)
b = int(b)
cnt = 0
sum = 0
result = []

for i in range(a,b+1):
    if isprime(i):
        cnt += 1
        sum += i
        result.append(i)

len = len(result)
cnt2 = 0
for i in result:
    cnt2 += 1
    if cnt2 == len:
        print("{}".format(i))
    elif cnt2 % 5 !=0:
        print("{} ".format(i),end='')
    else:
        print("{}".format(i))
        
print("amount={} sum={}".format(cnt,sum))


