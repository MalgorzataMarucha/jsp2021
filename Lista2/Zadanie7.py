lista = [(2,8),(5,5),(9,3),(1,0),(3,2),(6,4),(1,9),(10,3),(2,3),(1,7)]
def drugi_element(lista):
    return lista[1]
print(sorted(lista,key=drugi_element))