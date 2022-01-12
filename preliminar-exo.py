# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 15:32:46 2022

@author: Louis
"""

# Importation des modules
import random as rd

# Génerer un dictionnaire de 50 entrée aléatoire
d = {}
for i in range(50):
    d[rd.randint(0,255)] = "v"+str(i)


# Exo 1 & 2
count = 0
for keys in d:
    count = count + 1
    print(keys, end=" ")
print("\n", count)

# Exo 3
vref = int(input("Key value ? "))
vrefTest = []
vrefNear = 0
for keys in d:
    vrefTest.append(keys)
if vref > max(vrefTest) or vref < min(vrefTest):
    print("The key is not in the dictionary")
    if (vref - min(vrefTest)) < (max(vrefTest) - vref):
        vrefNear = min(vrefTest)
    else:
        vrefNear = max(vrefTest)
    print("The nearest value is", vrefNear)
else:
    vrefTest.append(vref)
    vrefTest.sort()
    print("The key is in the dictionary")
    vrefPosition = vrefTest.index(vref)
    vrefPositionMore = vrefPosition + 1
    vrefPositionLess = vrefPosition - 1
    if vrefTest[vrefPositionMore] - vrefTest[vrefPosition] < vrefTest[vrefPosition] - vrefTest[vrefPositionLess]:
        vrefNear = vrefTest[vrefPositionMore]
    else :
        vrefNear = vrefTest[vrefPositionLess]
    print("The closest number to the vRef is ", vrefNear)

