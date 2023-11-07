
money = input();

if money[0] == "$" :
    result = float(money[1:])*6
    print("R{:.2f}".format(result))
elif money[0] == "R":
    result = float(money[1:])/6
    print("${:.2f}".format(result))
