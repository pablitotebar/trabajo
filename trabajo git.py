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
print("\t6.- Resto                          --")
print("\t7.- Exponenciación de dos números  --")



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