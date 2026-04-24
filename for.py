# for i in range(1,6):
#     print(i)

# num=int(input("ingrese un numero"))
# for i in range(1, num+1):
#     print(f"{num} x {i} = {num*i}")

numN=int(input("Ingrese cantidad de notas")) 
for i in range(1,numN+1):
    nota=float(input("Ingrese su nota"))
    if numN>1:
        prom=float(nota+i/numN)
        print("su promedio es :",round(prom))
if prom<4.0:
    print("Estudiante reprobo")
else:
    print("Estudiante aprobo")


