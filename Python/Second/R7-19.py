n = input()
n = int(n)
n = abs(n)

result = {}
#字典key初始化
for i in range(0,10):
     result[i] = 0


#字典value给值
for i in str(n):
    result[int(i)] += 1

#输出
for i in range(0,10):
    print(f"{i} : {result[i]}")

