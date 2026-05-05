edad=0
Matricula=120000
PS=0
seguro_de_salud=25000
Descuento=float
Descuento2=float
print("Ingrese su edad")

edad=int(input())

print("Elige tipo de Plan")
print("1.- Elite")
print("2.- Pro")
print("3.- Basico")
PS=int(input())

if edad<=25:
    if PS== "1" or "2" :
        Descuento=Matricula*0.20
        Matriculafinal=Matricula-Descuento
        print("A su matricula se le descuenta :" , Descuento)
        print("El valor final de su matricula es : " , Matriculafinal)
    else :
        Descuento2=Matricula*0.10
        MatriBasica=Matricula-Descuento2
        print("A su matricula se le descuenta :" , Descuento2)
        print("El valor final de su matricula es : " , MatriBasica)







            

                


