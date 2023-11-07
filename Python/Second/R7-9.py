year = input()
mouth = input()
big = [1, 3, 5, 7, 8, 10, 12]
year = int(year)
mouth = int(mouth)

if mouth == 2:
    ri = 29 if year % 4 == 0 or year % 400 == 0 else 28
else:
    ri = 31 if mouth in big else 30

print("{}年{}月是{}天".format(year, mouth, ri), end='')


