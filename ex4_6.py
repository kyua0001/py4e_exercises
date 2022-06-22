def computepay(h, r):
    if h<=40:
        return h*r
    elif h>40:
        return 40*r + (h-40)*r*1.5

hrs = input("Enter Hours:")
fh = float(hrs)

rts = input("Enter Rates:")
fr = float(rts)

p = computepay(fh, fr)
print("Pay", p)
