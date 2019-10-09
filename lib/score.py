def score(filename):
    lines = open(filename).readlines()
    return lines


def countDuplicates(arrayCombined):
    num = 0
    i = 0
    transformToArray(arrayCombined[0], arrayCombined[1])
    while i < len(arrayCombined)-1:
        j = i + 1
        num = num + transformToArray(arrayCombined[i], arrayCombined[j])
        i=i+1
    return num    


def transformToArray(p1, p2):
    arrayRes = set(p1[1]).intersection(set(p2[1]))
    interseccion = len(list(arrayRes))
    list1 = len(p1)
    list2 = len(p2)
    num = min(interseccion, list1, list2)
    return num
