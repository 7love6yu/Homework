# str = input().split()

# list =list(str)

# for i in range(len(list)):
#     print(list[len(list)-i-1],end='')

# print()
# print(list)

# list.reverse()


# for i in range(len(list)-1):
#     print("{} ".format(list[i]),end='')
# i += 1
# print("{}".format(list[i]))

lst = input().split()

revslst = ''.join(lst[::-1])
revslstspace = ' '.join(lst[::-1])

print(revslst)
print(lst)
print(revslstspace)