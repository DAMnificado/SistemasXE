for i in range (1,6):
    print(i)

list = [1,2,3,4,5]
print(list)

for i in range (len(list)):
    list[i]=0

print(list)

'''for i in list:
    list[i]=0
'''

'''Eso es una tupla'''
list2 = (1,2,3,4)



'''STRING Y TUPLA NO ES MUTABLE'''
perro = 5
def cuidado(perro):
    perro = "pepe"
    return perro

print(cuidado("caca"))
print(cuidado(perro))
print(perro)



'''LISTA ES MUTABLE'''
def ojito():
    list[0]=1000


ojito()
print(list)

lista = True


def cambiarlista(lista):

   lista = False
   return lista

print(lista)
print(cambiarlista(lista))
print(lista)
