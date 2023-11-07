count = 0
for i in range(1,101):
    if i % 2 == 0:
        count+=1
        print("{} ".format(i),end='')
        if count % 5 ==0:
            print("")