autos={

    "A001" : ["Toyota" , "Corolla" ,2000,5  ] , 
    "A002" : ["Ford" , "Ranger" , 2019,4], 
    "A003" : ["Chevrolet", "Spark" , 2022,4] , 
    "A004" : ["Suzuki" , "Aerio",2005,4] , 
    "A005" : ["Toyota" , "Yaris" ,2015,5  ]

}


operaciones={
    "A001" : ["01-01-2024" , "12-12-2025" ] , 
    "A002" : ["07-08-2024 " , "01-08-2025"], 
    "A003" : ["09-01-2025" , "Pendiente"] , 
    "A004" : ["24-03-2025" , "Pendiente"] , 
    "A005" : ["24-03-2024" , "24-07-2024"  ]


}

def muestraautos(dic) : 
    for id , vehiculo in dic.items() :
        print(f"{id}.-{vehiculo}")


def autos_vendidos_por_marca(marca) :
    total = 0 

    for id_auto,datos in autos.items() : 

        if datos[0].lower() == marca.lower():

            if operaciones[id_auto][1] != "Pendiente" :

                total+=1

    print(f"el numero total de autos vendidos de la marca {marca.upper()} es {total} ")



marca=input("Ingrese la marca a buscar : ")
autos_vendidos_por_marca(marca) 

def busqueda_por_año(año_min,año_max) :
    elementos=[]
    
    for id_auto,datos in autos.items() :
        marca= datos[0]
        modelo= datos[1]
        año = datos[2]

        if año_min <= año <= año_max :
            if operaciones[id_auto][1] == "Pendiente" : 
                elementos.append(f"{marca} {modelo} -- {id_auto}")
    if elementos : 
        elementos.sort()
        print(elementos)

while True :

    try:

        año_inicio=int(input("Ingrese el año de inicio de la busqueda:"))
        año_termino=int(input("Ingrese el año de termino de la busqueda:"))
        busqueda_por_año(año_inicio,año_termino)
        break
    except : 
        print("Los datos ingresados deben ser numeros enteros")
print(operaciones)
id_auto=input("Ingrese el id del auto que desea actualizar :")

def actualizar_fecha_venta(id_auto) : 
    if id_auto in operaciones :
        nueva_fecha=input("Ingrese la nueva fecha del auto : ")
        operaciones[id_auto][-1]=nueva_fecha
        return True
    else :
        print("El id no se encuentra ")
        return False


while True : 
    id=input("Ingrese el valor del ID a actualizar :")
    fecha=input("Ingrese la fecha a actualizar :")

    if actualizar_fecha_venta(id,fecha) :
        print("Actualizado correctamente")
    else : 
        print("El id no se encuentra ")
    next=input("¿Desea actualizar otro vehiculo?(s/n)")
    if next.lower() == "n" : 
        break


def validaAÑO(a):
    if a<1900 :
        return True
    else:
        return False

def validaRanking(a):
    if a < 1 and a >6 :
        return True
    else:
        return False


def validaString(s) :
    if s == "" or s == " " :
        return True
    else : 
        return False




def creauto() : 
    id=input("Ingrese el ID:")
    if validaString(id) : 
        print("Dato incorrecto")
        return
    marca=input("Ingrese la marca : ")
    if validaString(marca) : 
        print("Dato incorrecto")
        return
    modelo=input("Ingrese el modelo : ")
    if validaString(modelo) : 
        print("Dato incorrecto")
        return
    año=int(input("Ingrese el año : "))
    if validaAÑO(año) : 
        print("El año debe ser superior a 1900")
        return
    ranking=int(input("Ingrese el ranking : "))
    if validaRanking(ranking) :
        print("El ranking tiene que ser un numero entero entre 1 y 5")
        return
    fecha=input("Ingrese la fecha ")
    autos[id]=[marca,modelo,año,ranking]
    operaciones[id]=[fecha,"Pendiente"]





def eliminar_auto(id_auto) :
    if id_auto in autos :
       del autos[id_auto]
       del operaciones[id_auto]
       return True
    else : 
        return False




# Menu principal 
while True :
    print("=====Menu Principal=====") 
    print("1.-Autos vendidos por marca")
    print("2.-Busqueda por año ")
    print("3.-Actualizar fecha de venta")
    print("4.-Añadir auto")
    print("5.-Eliminar auto")
    print("6.-Salir")

    op=int(input("Elija una opcion "))
    if op == 1 : 
        autos_vendidos_por_marca() 
    elif op == 2 : 
        busqueda_por_año()
    elif op == 3 : 
        actualizar_fecha_venta()
    elif op == 4 : 
        creauto()
    elif op == 5 : 
        eliminar_auto() 
    elif op == 6 : 
        break
        
