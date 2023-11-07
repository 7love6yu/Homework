str = input()
digit = 0
alpha = 0
space = 0
hz = 0
expect = 0

for char in str:
    if char.isdigit():
        digit += 1
    elif char >= '\u4e00' and char <= '\u9fa5': #需要写在前边
        hz += 1
    elif char.isalpha():
        alpha += 1
    elif char.isspace():
        space += 1
    else:
        expect +=1

print(f"您输入的字符串中有{space}个空格,{digit}个数字,{hz}个中文,{alpha}个英文字符,{expect}个其他字符",end='')


