#coding: utf8
#Carlos león olivares

import os
os.system ("clear")
from math import pi 

print """
 ┌──────────────────────────┐
 │  Calculadora de áreas    │    
 └──────────────────────────┘
 Selecciona la tecla T para calcular el área de un triángulo.
 Selecciona la tecla C para calcular el área de un círculo.
 
"""
figura=raw_input("Que quieres calcular? ")
 
if(figura=="T" or figura=="t"):
	base=input("Escriba la base: ")
	altura=input("Escriba la altura: ")
	if(base<0 or altura<0):
		print "Uno de los valores es negativo"
	else:
		print "Un triangulo de base",base,"y altura",altura,"tiene un área de" ,round(base*altura/2,2)
else:
	if(figura=="C" or figura=="t"):
		radio=input("Escriba el radio: ")
		if(radio<0):
			print "El radio de un circulo no puede ser negativo"
		else:
			print "Un circulo de radio",radio,"tiene un área de" ,round(pi*radio**2,2)
	else:
		print "Porfavor selecciona triángulo o círculo"
    
    
