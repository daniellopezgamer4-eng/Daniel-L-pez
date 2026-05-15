# while True:
#     try:
#         num=int(input("Ingrese un numero :"))
#         break
#     except:
#         print("Solo numeros enteros")


code=6767
while True:
    try:
        passw=int(input("Ingrese su clave"))
        if code==passw:
            print("Ingreso correcto")
            break 
        else:
            print("Clave invalida") 
    except ValueError as er:
        print("solo numero enteros ")
        print(er)
