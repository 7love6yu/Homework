def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return  1
    else:
        return  fib(i-1)+fib(i-2)


for i in range(0,12):
    res = fib(i)
    print("{}   ".format(res),end='')
