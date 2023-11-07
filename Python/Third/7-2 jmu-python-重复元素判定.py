# def pan(lst):
#      lst_set = set(lst)
#      if(len(lst) == len(lst_set)):
#         return False
#      else:
#         return True

def isUnion(lst):
    return len(lst) != len(set(lst))
    
n = int(input())
cntf = 0 
cntt = 0

for _ in range(n):
    lst = input().split()
    if(isUnion(lst)):
        cntt += 1
    else:
        cntf += 1

print("True={}, False={}".format(cntt,cntf))