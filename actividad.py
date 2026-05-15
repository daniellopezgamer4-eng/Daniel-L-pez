while True:
    try:
        pasajes=int(input("Cuantos pasajes desea vender: "))
        break
    except:
        print ("Dato invalido, Intente denuevo")



subtotal=0
for i in range (1, pasajes+1):
    while True:
        try:
            valor = int(input(f"Ingrese valor del pasaje {i}: "))
            break
        except:
            print("Error, Intente denuevo")
        
    subtotal = subtotal+valor

print(f"La cantidad recolectada fue de: {subtotal}$")
