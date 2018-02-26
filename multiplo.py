#coding: utf8
#Carlos León

valor1=input("Escribe el primer valor: ")
valor2=input("Escribe el segundo valor: ")

if(valor1==0 or valor2==0):
	print "Ningun valor puede ser 0"
elif(valor1<0 or valor2<0):
    print "Uno de los valores es negativo"
else:
	if(valor1>valor2):
		num1=valor1
		num2=valor2
	else:
		num1=valor2
		num2=valor1
		
	if(num1%num2==0):
		print num1,"es multiplo de ",num2
	else:
		print num1,"no es multiplo de ",num2
		
