# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:19:48 2022

@author: PabloMuñozTébar
"""
print("\t1.- Suma de dos números            --")
print("\t2.- Resta de dos números           --")
print("\t3.- Multiplicación de dos números  --")
print("\t4.- División de dos números        --")

print("\t5.- Cociente 2                      --")
print("\t5.- Cociente 1                       --")

print("\t6.- Resto     2                     --")
print("\t7.- Exponenciación de dos números  --")
print("\t8.- Area triangulo                 --")
print("\t9.- Area circulo                   --")





opc = int(input("Introduzca una opción: "))
if(opc==1):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}+{y}={x+y}")
    
elif(opc==2):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}-{y}={x-y}")
    
elif(opc==3):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}*{y}={x*y}")
    
elif(opc==4):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}/{y}={x/y}")
    if(y==0):
        print("0 es un numero valido")
    else:
        print("El resto es: ")

elif(opc==5):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}//{y}={x//y}")
    if(y==0):
        print("0 es un numero valido")
    else:
        print("El resto es: ")
        
elif(opc==6):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}%{y}={x%y}")
    if(y==0):
        print("0 es un numero valido")

elif(opc==7):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}*{x}={x*x}")
    print(f"{y}*{y}={y*y}")

elif(opc==8):
    listaTriangulos=[(3,2),(1,5),(6,7)]
    for triangulo in listaTriangulos:
        areaTriangulo=triangulo[0]*triangulo[1]/2
        print(f"El área del triángulo de base {triangulo[0]} y altura {triangulo[1]} es {areaTriangulo} metros cuadrados")
        
elif(opc==9):
    import math
    listacirculo=[3,6,1,9,5]
    for circulo in listacirculo:
        print(circulo*circulo*math.pi)