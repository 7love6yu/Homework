# 补零失败
# a,b = input().split()
# result = []
# a = list(a)
# b = list(b)

# a.reverse()
# b.reverse()

# if len(a) > len(b):
#     sub = len(a) - len(b)
#     for f1 in range(0, sub):
#         a.append(0)
# elif len(b) > len(a):
#     sub2 = len(b) - len(a)
#     for f2 in range(0, sub2):
#         b.append(0)

# for i in range(0, max(len(a),len(b))):
#     result.append(int(a[i]) * int(b[i]))

# sum = sum(result)
# print(sum)




# 算法
# a,b = map(int,input().split())

# a = abs(a)
# b = abs(b)
# sum = 0

# while True:
#     if a == 0 or b == 0:
#         break
#     sum += (a%10)*(b%10)
#     a = a//10
#     b = b//10

# print(sum)



#字符串
#第二个测试点为负数
#第三个测试点为相等长度

a,b = map(int,input().split())
a,b= abs(a),abs(b)
str_a,str_b = str(a),str(b)

i = 0
result = 0

while i < len(str_a) or i < len(str_b):
    rsta = int(str_a[-1-i]) if i < len(str_a) else 0
    rstb = int(str_b[-1-i]) if i < len(str_b) else 0
    result += rsta * rstb
    i+=1

print(result)
    