import math
#Fragmentation Calculator
ρ= float(input("Insert Provide In-Hole Density(kg/m³):"))
BH=float(input("Insert Bench Height(m):"))
E=float(input("Insert Relative Effective Energy of Explosive(E):"))
SL= float(input("Stemming Length(m):"))
BD=float(input("Blasting Diameter (m):"))
K= float(input("Insert Actual Powder Factor:"))
#Determining the rock type and factor
def RockFactor():
    RockType = input("Insert rock type (hard/medium/soft/very soft): ").lower()
    if RockType == "very soft":
        return 6
    elif RockType == "soft":
        return 8
    elif RockType == "medium":
        return 10
    elif RockType =="hard":
       return 12
    else:
        print("Rock type is invalid!")
A = RockFactor()
#Calculate Q/explosive mass per hole (kg)
Q=ρ* (math.pi * BD**2 / 4) * (BH - SL)
#Kuznetsov equation for mean fragment size
X50 = A*K ** (-0.8) * Q ** (1 / 6) * (116 / E) ** (19 / 30)
print("mean fragment size=",X50)
