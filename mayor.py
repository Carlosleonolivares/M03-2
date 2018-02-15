#coding: utf8
#Carlos León Olivares 09/02/2018

a=input("Introduce el primer número")
b=input("Introduce el segundo número")
c=input("Introduce el tercer número")

if(a>b) and (a>c):
    print "El primer valor és el más grande."
else:
    if(b>a) and (b>c):
        print "El primer valor és el más grande."
    else:
	print "El tercer valor és el más grande."
		
if(a<b) and (a<c):
    print "El primer valor és el más pequeño."
else:
    if(b<a) and (b<c):
        print "El segundo valor és el más pequeño."
    else:
	print "El tercer valor és el más pequeño."
		

if(a==b):
    print "El primer y segundo valor se repiten"
else:
    if(a==c):
        print "El primer y tercer valor se repiten"
    else:
	if(b==c):
	    print "El segundo y tercer valor se repiten"
	else:
            if(a==b) and (a==c):
		print "Todos los valores se repiten"
