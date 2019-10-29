def computepay(hrs,rate):
    if fhrs > 40:
        over_time = (fhrs - 40) * (frate * 1.5)
        pay = (40 * frate) + over_time
    elif fhrs <= 40:
        pay = fhrs * frate
    return pay
hrs = input("Enter Hours:")
rate = input("Enter Rate per hour:")
fhrs=float(hrs)
frate=float(rate)
p=computepay(hrs,rate)
print(p)
