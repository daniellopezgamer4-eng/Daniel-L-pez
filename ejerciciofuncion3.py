Juegos={
    "Hackandslash":"Devil may cry 3 ",
    "run and gun": "Cuphead" ,
    "Plataformer" : "Super mario galaxy" , 
    "Rpg": "Final fantasy 7"
}

def agregar():
    Juegos["Sandbox"]="Minecraft"

def borrar():
    eliminar=input("Que desea eliminar?")
    if eliminar in Juegos.keys() :
        del Juegos[eliminar]

def actualizar():
    actualizar=input("Que genero desea actualizar?") 
    if actualizar in Juegos.values() :
        Juegos[actualizar] 
         

def mostrar() :
    print(Juegos)

while True:
    print("1.- Agregar dato")
    print("2.- Borrar datos")
    print("3.-Actualizar")
    print("4.-Mostrar datos")
    print( "5.-Salir") 
    op=int(input("Elija una opcion"))
    for key, value in Juegos.items():
        print(key, value)
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
        

    
# print(Juegos["Hackandslash"])

     
# del Juegos ["Plataformer"] 

     
# Juegos["Rpg"]="Final Fantasy Remake Integrade" 

# Juegos["Sandbox"]="Minecraft" 

# print(Juegos)
        
    
     

