#coding: utf8
#Carlos León Olivares 09/02/2018

a=input("Introduce el primer número: ")
b=input("Introduce el segundo número: ")
c=input("Introduce el tercer número: ")

if(a>b) and (a>c):
    if (b>c):
        print "El tercer valor és el más pequeño."
    else:
		print "El primer valor és el más grande."
else:
	if(b>a) and (b>c):
	    if (c>a):
			print "El primer valor és el más pequeño."
        else:
			print "El segundo valor és el más grande."
    else:
		if (a>b):
		    print "El segundo valor es el más pequeño"
		else: 
			print "El tercer valor és el más grande."
		

		


	
