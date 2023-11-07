def panda(lst):
    for i in lst:
        if type(i) is tuple or type(i) is list:
            panda(i)
        elif type(i) is float or type(i) is int:
            result.append(i)

lst = eval(input())
result = list()
panda(lst)
print(sum(result))