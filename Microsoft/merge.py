import unittest
def merge(lista, listb):
    if not isinstance(lista, list) and not isinstance(listb, list):
        raise ValueError
    else:
        listc = list()
        for i in lista: 
            listc.append(i)
        
        for i in listb:
            listc.append(i)
    lista.extend(listb)
    listc = sorted(lista)
    return sorted(listc)

print(merge([1, 4, 6], [5, 8, 12]))