import numpy as np
import itertools
def imprime_renglon(renglon,size=4):
    a=""
    for i in renglon:
        a +=  i
    a+="\n"
    return a

#quito repetidos
def Quitar_repetidos(a):
    result = []
    for item in a:
        if item not in result:
            result.append(item)
    return result

def regresaLista(Lista, Sustituto):
    regreso =[]
    for b in Lista:
       for i in range(len(b)):
            b = np.array(b)
            a = b.copy()
            a[i] = Sustituto
            regreso.append(a.tolist())
    return regreso

def regresaLista2(Lista, Sustitutos):
    regreso =[]
    for b in Lista:
       for i in range(len(b)):
            for sus in Sustitutos:
                b = np.array(b)
                a = b.copy()
                a[i] = sus
                regreso.append(a.tolist())
    return regreso


renglon     =["H     ","H     ","H      ","H     " ]
grupos      =["OH    ","SH    ","NH2    ","COOH  "]
a =[]
a.extend([renglon])



#Cada uno funciona por separado, pero cada funcion es 
for i  in range (len(grupos)):
    a.extend(regresaLista2(a,grupos))
    a.extend( list(itertools.chain(*list(map( lambda x:   regresaLista(a,x), grupos  )))))

print(len(a))
a =[]
a.extend([renglon])
for i  in range (len(grupos)):
    a.extend(regresaLista2(a,grupos))
    a = Quitar_repetidos(a)
print(len(a))
a =[]
a.extend([renglon])

a.extend( list(itertools.chain(*list(map( lambda x:   regresaLista(a,x), grupos  )))))
a = Quitar_repetidos(a)

a.extend(regresaLista2(a,grupos))
a = Quitar_repetidos(a)

a.extend( list(itertools.chain(*list(map( lambda x:   regresaLista(a,x), grupos  )))))
a = Quitar_repetidos(a)


a.extend(regresaLista2(a,grupos))
a = Quitar_repetidos(a)

print(len(a))

'''for i in a:
    print(imprime_renglon(i))'''