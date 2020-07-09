import listaPersonas
import libros


datos = {'a':'Ver lista de personas',
    'b':'Ordenar lista de personas',
    'c':  'Imprimir registro de lista de personas',
    'd':  'Ver lista de libros',
    'e':  'Buscar libro',
    'f':  'Prestar libro',
    'g':  'Ver prestamo de libros'}

print(datos)



print("Digite la letra para ingresar:")

Introducir = str(input())

def seleccione(Opcion):
    if Opcion == 'a':
        listaPersonas.ver_lista()        
    if Opcion == 'b':
        listaPersonas.ordenar_personas()        
    if Opcion == 'c':
        listaPersonas.registro_personas()        
    if Opcion == 'd':
        libros.lista_libros()        
    if Opcion == 'e':
        libros.Buscar_libro()        
    if Opcion == 'f':
        libros.Prestar()        
    if Opcion == 'g':
        libros.prestamos_libros()        




seleccione(Introducir)
