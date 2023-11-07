import math

n = int(input(""))
result = 1.0;

k = 2

for  i  in range(2,n+1,2):
     result *= (k/(k-1)) * (k/(k+1))
     k +=2;

result = result * 2


print("{:.12f}".format(result),end='')
# format 自带四舍五入
