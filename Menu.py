import Personas
import Lista_Libros

Menu = {'a': 'a - Ver lista de personas','b': 'b - Ordenar lista de personas','c': 'c - Imprimir registro de lista de persona','d': 'd - Ver lista de libros',
    'e': 'e - Buscar libro','f': 'f - Prestar libro','g': 'g - Ver prestamo de libros','h': 'h - Salir'}

def Seleccion(Seleccionar):
    if Seleccionar == "a":
        Personas.ImprimirLista()
        print(" ")
    elif Seleccionar == "b":
	   	Personas.Ordenar()
    elif Seleccionar == "c":
       Personas.Registro()
       print(" ")
    elif Seleccionar == "d":
        Lista_Libros.Imprimir_Lista()
        print(" ")
    elif Seleccionar == "e":
        Lista_Libros.Buscar_Libro()
        print(" ")
    elif Seleccionar == "f":
        Lista_Libros.prestar_libro()
        print(" ")
    elif Seleccionar == "g":
        Lista_Libros.Imprimir_Prestados()
        print(" ")
    elif Seleccionar == "h":
        exit()
               

Activar = True 
while (Activar == True):
    print("Menú Principal: ")
    print (Menu)
    print(" ")
    print(" ")
    print("Seleccione una de las opciones del menú: ")
    Opcion = str(input())
    Seleccion(Opcion)

    if Opcion == "h":
        Activar = False