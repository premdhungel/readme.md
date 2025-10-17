hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric value")
    quit()
print(h, r)
pay = 0
if h<=40:
    pay = r*h
else:
    pay =r*40 + 1.5*r*(h-40)
print(pay)