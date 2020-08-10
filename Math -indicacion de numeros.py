
a = int(input("Ingrese el primer valor a : "))
b = int(input("Ingrese el valor b: "))

if a%2==0 and b%2==0: # si a/2 es igual a 0 y b/2 es igual a 0, entonces:
    print("los numeros son pares")

elif (a%2==0 and b%2!=0) or (a%2!=0 and b%2==0): #si a/2 da resto 0 y el resto de b/2 es distinto de 0 , o, el resto de a/2 es distinto de 0 y b/2 da resto 0, entonces:
    print("Uno de los numeros es impar")

else:

  print("Ninguno de los numeros digitados es par.")
