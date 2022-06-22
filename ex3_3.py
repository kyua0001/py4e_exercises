# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

Score = input("Enter Score:")
fs = float(Score)

if fs>=0.9:
    print("A")
elif fs>=0.8:
    print("B")
elif fs>=0.7:
    print("C")
elif fs>=0.6:
    print("D")
elif fs<0.6 and fs>=0:
    print("F")
else:
    print("ERROR")
