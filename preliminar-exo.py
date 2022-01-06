# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:32:46 2022

@author: Louis
"""

d= {5: "v1",30: "v2",2: "v3", 50: "v4", 90: "v5", 70: "v6"}

# Exo 1 & 2
count = 0
for keys in d:
    count = count + 1
    print(keys, end=" ")
print("\n", count)

# Exo 3
vref = int(input("Key value ? "))
vrefTest = []
for keys in d:
    vrefTest.append(keys)
vrefTest.append(vref)
vrefTest.sort()
vrefPosition = vrefTest.index(vref)
vrefPositionMore = vrefPosition + 1
vrefPositionLess = vrefPosition - 1
if vrefTest[vrefPositionMore] - vrefTest[vrefPosition] < vrefTest[vrefPosition] - vrefTest[vrefPositionLess]:
    vrefNear = vrefTest[vrefPositionMore]
else :
    vrefNear = vrefTest[vrefPositionLess]
print("The closest number to the vRef is ", vrefNear)


# Exo 4
    