import random as rd
# Fonction de génération d'un dictonnaire aléatoire entre 0 et 255 inclut
def gen_dict(n):
    d = {}
    for i in range(n):
        d[rd.randint(0,255)] = "v"+str(i)
    return d

# Fonction qui trouve la vignette de dico la plus proche de la valeur vref et retourne vignette
def find_nearest(d, vref):
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
    return vrefNear

vref = 45
dico = gen_dict(50)
vignette = find_nearest(dico, vref)
print("La vignette la plus proche de", vref, "est", vignette)