a, b, c = input().split()
#注意 必须使用分割默认参数！ PTA不然会报错
a = int(a)
b = int(b)
c = int(c)
deta = b * b - 4 * a * c

if deta > 0:
    x1 = (-b + deta ** 0.5) / (2 * a)
    x2 = (-b - deta ** 0.5) / (2 * a)
    print("x1={:.3f}".format(x2))
    print("x2={:.3f}".format(x1))
elif deta == 0:
    x = -b / (2 * a)
    print("x={:.3f}".format(x))
else:
    print('no real solution')


