a,b = input("").split(":")
a = int(a)
if a == 0 :
    a = 12
    print("{}:{} AM".format(a, b))
elif a ==12 :
    print("{}:{} PM".format(a, b))
elif a>12:
    a -= 12
    print("{}:{} PM".format(a,b))
elif a<12:
    print("{}:{} AM".format(a, b))