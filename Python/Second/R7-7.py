def issan(a):
    a_str = str(a)
    if len(a_str) != 3:
        return True
    else:
        return False

a = input()
a = int(a)

bai = a//100%10
shi = a//10%10
ge = a%10

pan = bai*bai*bai+shi*shi*shi+ge*ge*ge

if pan == a :
    print(f"该数是水仙花数")
elif issan(a):
    print(f"输入错误，不是一个三位数")
else:
    print(f"该数不是水仙花数")
