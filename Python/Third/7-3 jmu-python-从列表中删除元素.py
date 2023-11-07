#本程序正常可以在循环内边输入边输出
#PTA不验证时候一次性输出还是在循环内输出
#若循环内输出可以用join连接为字符串输出
#PTA追加空行判断语句是一行真正为空 空格也没有

n = int(input())
# results = []

for _ in range(n):
    lst = input().split()
    delElem = input()
    result = [i for i in lst if delElem != i]
    if result:
        # results.append(" ".join(result))
        print(" ".join(result))
    else:
        # results.append("")
        #追加空行使用”“为缺省值
        print("")

# for res in results:
#     print(res)