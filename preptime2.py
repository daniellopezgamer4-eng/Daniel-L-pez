# Cantidad de registros 
# print("Cuantos registros vas a procesar?") 
# while True :
#     try :
#         re=int(input("Cantidad de registros:"))
#         break 
#     except ValueError as er :
#         print("¡Número inválido! Ingresa un entero positivo para continuar el entrenamiento")

# if re <0 :
#    print("¡Número inválido! Ingresa un entero positivo para continuar el entrenamiento") 

nombrec=input("Cual es el nombre de la ciudad(Al menos 6 caracteres y sin espacios):").upper() 
nombrec=nombrec.replace(" "," ")
while " " in nombrec or len(nombrec)<6:
    print("No de incluir espacios")
    nombrec=input("Ingrese el nombre del juego (Al menos 6 caracteres y sin espacios): ").upper()