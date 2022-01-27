# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:19:48 2022

@author: PabloMuñozTébar
"""
print("\t1.- Suma de dos números            --")
print("\t2.- Resta de dos números           --")
opc = int(input("Introduzca una opción: "))
if(opc==1):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}+{y}={x+y}")
    
elif(opc==2):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    print(f"{x}-{y}={x-y}")