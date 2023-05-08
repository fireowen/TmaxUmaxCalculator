from math import *



def Tmax(r, H, Q, Tinf):
    ratio = r / H

    if ratio < 0.18:
        result = ((16.9 * Q ** (2 / 3)) / (H ** (5 / 3))) + Tinf
    else:
        result = ((5.38 * ((Q / r) ** (2 / 3))) / (H)) + Tinf

    return result


def Umax(r, H, Q, Tinf):
    ratio = r / H

    if ratio < 0.15:
        result1 = 0.96 * (Q / H) ** (1 / 3)
    else:
        result1 = (0.195 * Q ** (1 / 3) * H ** (1 / 2)) / (r ** (5 / 6))

    return result1


'''
r = float(input("Input r: "))
H = float(input("Input H: "))
Q = float(input("Input Q: "))
Tinf = float(input("Input Tinf: "))

ratio = r / H
print("r/h = " + str(ratio))

print("Tmax = " + str(Tmax()))

print ("Umax = " + str(Umax()))


'''
