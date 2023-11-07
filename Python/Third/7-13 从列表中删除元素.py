n = int(input())

for _ in range(n):
    lst = input().split()
    x = input().strip() #防止去space
    result = [elme for elme in lst if elme != x]
    # 条件创建列表
    if result:
        print(" ".join(result))
    else:
        print()
