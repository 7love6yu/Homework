#eval处理的数据是int类型
#正常input.split处理的数据是str类型
lst = set(eval(input()))
#列表推导强转str连接输出
print(",".join([str(i) for i in lst]))
