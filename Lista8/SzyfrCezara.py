def szyfr(tekst,klucz):
    lista=[]
    for x in tekst:
        if(ord(x)>=65 and ord(x)<=90):
            zmien=ord(x)
            zmien+=klucz
            if(zmien>90):
                zmien-=26
                lista.append(chr(zmien))
            else:
                lista.append(chr(zmien))
        elif(ord(x)>=97 and ord(x)<=122):
            zmien=ord(x)
            zmien+=klucz
            if(zmien>122):
                zmien-=26
                lista.append(chr(zmien))
            else:
                lista.append(chr(zmien))
        elif(ord(x)>=0 and ord(x)<65 or ord(x)>90 and ord(x)<97 or ord(x)>122):
            lista.append(x)
    return "".join(lista)
def deszyfr(tekst,klucz):
    lista2=[]
    for x in tekst:
        if(ord(x)>=65 and ord(x)<=90):
            zmien=ord(x)
            zmien-=klucz
            if(zmien<65):
                zmien+=26
                lista2.append(chr(zmien))
            else:
                lista2.append(chr(zmien))
        elif(ord(x)>=97 and ord(x)<=122):
            zmien=ord(x)
            zmien-=klucz
            if(zmien<97):
                zmien+=26
                lista2.append(chr(zmien))
            else:
                lista2.append(chr(zmien))
        elif(ord(x)>=0 and ord(x)<65 or ord(x)>90 and ord(x)<97 or ord(x)>122):
            lista2.append(x)
    return "".join(lista2)
