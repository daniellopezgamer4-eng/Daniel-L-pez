indie=0
estudio=0


print("Registro de juegos") 

while True :
    try :
        cantidadjuegos=int(input("Cuantos juegos son? :" ))
        break
    except ValueError as er :
        print("numero de juegos invalidos")
        
for i in range(cantidadjuegos) :
    nombrej=input("Cual es el nombre de los juegos : ")

while True:
    try :
        for i in range(cantidadjuegos):

            preciojuego=int(input("Cuanto vale el juego :"))
            if 20000 <= preciojuego <40000 : 
                print("Tu juego es indie ")
                indie+=1
            elif preciojuego >= 40000 :
                print("Tu juego es de estudio")
                estudio+=1
            break 
    except ValueError as er :
            print("Coloque un precio o caracter valido")














    

