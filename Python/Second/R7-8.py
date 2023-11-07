score = int(input())

if score < 0 or score > 100:
    print("输入成绩不在0到100之间！")
elif score >= 90:
    print("{}分是优秀！".format(score))
elif score >= 80:
    print("{}分是良好！".format(score))
elif score >= 70:
    print("{}分是中等！".format(score))
elif score >= 60:
    print("{}分是及格！".format(score))
else:
    print("很遗憾！{}分不及格！".format(score))