#Pay 1.5 times the hourly rate for hours > 40
hrs = input("Enter hours:")
fh = float(hrs)

rate = input("Enter rate:")
fr = float(rate)

if fh>40:
    pay = 40*fr + (fh-40)*fr*1.5
else:
    pay = fh*fr
print("Pay:",pay)
