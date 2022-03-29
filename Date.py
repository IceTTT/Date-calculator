from datetime import date ,timedelta

x = int(input("enter years pls: "))
if x > 9999 or x < 0000 :
    print("year available from 1900 to 2022")
    exit()


y = int(input("enter month pls: "))
if y > 12 or y < 1 :
    print("month available from 1 to 12")
    exit()


z = int(input("enter days pls: "))
if z > 1000:
    print("max 1000 days")
    exit()

g = input("inter (+) if you want to addition\ninter (-) if you want to Subtraction\n")


r = int(input("enter the other days: "))

if g == "+" :
    d1 = date(x, y, z)
    s = d1 + timedelta(r)
    print(s)
elif g == "-" :
    d1 = date(x, y, z)
    s = d1 - timedelta(r)
    print(s)