libros = [
{"nombre": "Cien años de soledad"},
{"nombre": "Don Quijote de la Mancha"},
{"nombre": "Hamlet"},
{"nombre": "El Principito"},
{"nombre": "Orgullo y Prejuicio"},
{"nombre": "1984"},
{"nombre": "La Odisea"},
{"nombre": "El retrato de Dorian Grey"},
{"nombre": "Lo que el viento se llevó"},
{"nombre": "Moby-Dick" } ]


print ("Que quiere buscar: ")
texto = str (input ())

l = 0
while (l < len(libros)):
  if(libros[l]["nombre"].find(texto) >= 0):
    print(libros[l])
  l = l + 1