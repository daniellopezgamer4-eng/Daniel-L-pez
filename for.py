# for i in range(1,6):
#     print(i)

# num=int(input("ingrese un numero"))
# for i in range(1, num+1):
#     print(f"{num} x {i} = {num*i}")

# numN=int(input("Ingrese cantidad de notas")) 
# for i in range(1,numN+1):
#     nota=float(input("Ingrese su nota"))
#     if numN>1:
#         prom=float(nota*i/numN)
        
# if prom<4.0:
#     print("su promedio es :", prom)
#     print("Estudiante reprobo")
# else:
#     print("su promedio es :", prom)
#     print("Estudiante aprobo")


num=int(input("Ingrese un numero"))
total=0
for i in range(num):
    total+=i+1 
    print(f"el resultado total es {total}" )