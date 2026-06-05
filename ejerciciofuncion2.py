# lista=[1,2,3,4,5,6,7,8,9,10]

# import time
# print(lista)
# print(lista[-4])

# for i in lista:
#     if i%2==0 :
#         print(i , "Es par ")
#     else:
#         print(i , "Es impar ")
#         time.sleep(1)

# nombres=["Amaro" , "Carlos" , "Yony"]
# apellidos=["Vega" , "Castillos" , "Paredes" ]

# print(nombres)
# print(nombres[0] , apellidos[0])

# for n in range(len(nombres)):
#     print(nombres[n] , apellidos[n])

frutas=["Kiwi" , "Pera" , "Melon" , "Uva"]
print(frutas)


for i in range(len(frutas)) :
    print(frutas[i])

var=input("Añada una fruta a la lista : ") 
frutas.append(var)
for i in range(len(frutas)) :
    print(frutas[i])

# for i in frutas:
#     if i [-1].lower()=="a":
#         print(i, "termina con a")
#     else :
#         print(i, "No termina con a") 

vocales="aeiou"
for i in frutas :
    if i [0].lower() in vocales:
        print(i , "Empieza por vocal")
    else:
        print(i , "No empieza por vocal ")

