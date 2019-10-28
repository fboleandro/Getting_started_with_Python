hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)
if h > 40 :
    reg = h * r
    opt = (h - 40) * (r * 0.5)
    xp = reg + opt
else:
    xp = reg * opt
print(xp)
