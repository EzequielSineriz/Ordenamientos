""" ORDENAMIENTOS
Ejercicio 1: Dadas las siguientes listas:
Nombres =
["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Anto
nio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente. """
#Nombres =["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
#Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def burbujeo_acendente_dos_lista(lista_uno:list,lista_dos:list)->list:
    for i in range(len(lista_uno)-1):
        for j in range(i+1,len(lista_uno)):
            if lista_uno[i] > lista_uno[j]:
                swapear_lista(lista_uno,i, j)
                swapear_lista(lista_dos,i ,j)
                

def swapear_lista(lista:list, posicion_primera:int, posicion_segunda:int):
    aux = lista[posicion_primera]
    lista[posicion_primera] = lista[posicion_segunda]
    lista[posicion_segunda] = aux
    return lista
""" 
def burbujeo_decendente(lista:list)->list:
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux """

""" print(Edades)

burbujeo_decendente(Edades)

print(Edades) """



"""" Ejercicio 2: Dadas las siguientes listas:
Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias
Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
"Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
Desarrollar una función que realice el ordenamiento de las listas por nombre de
manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
descendente """

Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
"Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def burbujeo_acendente_lista_puntos(lista:list, lista_2:list, puntos:list)->list:
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                swapear_lista(lista)
                swapear_lista(lista_2)
                #swapear la otra lista
            if lista[i] == lista[j]:
                if puntos[i] < puntos[j]:
                    swapear_lista(lista)
                    swapear_lista(lista_2)


           
def burbujeo_decendente(lista:list)->list:
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux      



#burbujeo_acendente_lista_puntos(Nombres, Puntos)

#print([Nombres, Puntos])


Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
""" Desarrollar una función que realice el ordenamiento de las listas por apellido de
manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
ascendente, si el nombre también es el mismo, debe ordenar por nota de manera
descendente. """

def burbujeo_tres_listas(lista_a:list, lista_b:list, lista_c:list):
    for i in range(len(lista_a)-1):
        for j in range(i+1,len(lista_a)):
            if lista_a[i] > lista_a[j]:
                swapear_lista(lista_a)
                swapear_lista(lista_b)
                swapear_lista(lista_c)
            if lista_a[i] == lista_a[j]:
                if lista_b[i] > lista_b[j]:
                    swapear_lista(lista_a)
                    swapear_lista(lista_b)
                    swapear_lista(lista_c)
                if lista_b[i] == lista_b[j]:
                    if lista_c[i] < lista_c[j]:
                        swapear_lista(lista_a)
                        swapear_lista(lista_b)
                        swapear_lista(lista_c)




