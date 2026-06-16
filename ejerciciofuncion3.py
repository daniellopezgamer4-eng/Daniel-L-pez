Juegos={
  "Hackandslash":"Devil may cry 3 ",
  "run and gun": "Cuphead" ,
  "Plataformer" : "Super mario galaxy" ,
  "Rpg": "Final fantasy 7"
}
 
 
 
 
def agregar():
  genero = input("Genero que desea añadir? :")
  juego = input("juego que sea del genero añadido : ")
  Juegos[genero]= juego
 
 
 
 
def borrar():
  eliminar=input("Indique genero que desea eliminar: ")
  if eliminar in Juegos.keys() :
    del Juegos[eliminar]
 
 
 
def actualizar():
  genero=input("¿Que genero desea actualizar?: ")
  juego = input("Nuevo nombre del juego : ")
  if genero in Juegos :
    Juegos[genero]=juego
    print('entrando')
 
 
def mostrar() :
  print()
  print('Lista de juegos:')
  print('----------------')
  for key, value in Juegos.items():
    print(key,' - ', value)
  print()
 
 
 
while True:
  print()
  print("1.- Agregar dato ")
  print("2.- Borrar datos ")
  print("3.- Actualizar ")
  print("4.- Mostrar datos ")
  print("5.- Salir")
  print()
 
 
  op=int(input("Elija una opcion: "))
 
 
 
 
  if op == 1 :
    agregar()
 
 
  elif op == 2 :
    borrar()
 
 
  elif op == 3 :
    actualizar()
 
 
  elif op == 4 :
    mostrar()
 
 
  elif op == 5 :
    break
 
