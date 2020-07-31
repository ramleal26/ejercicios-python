#a = float(input("Digite un valor x: "))
#b = float(input("Digite otro valor x: "))

#operacion = input("Digite que operacion desea realizar: ").lower()

#if operacion=='suma':
 #print(f"El resultado de la suma es {a+b}")

#elif operacion=='resta':
     #print(f"El resultado de la resta es {a-b}")
#elif operacion=='multiplicacion':
     #print(f"El resultado de la multiplicacion es {a*b}")
#elif operacion=='division':
     #print(f"El resultado de la division es {a/b:.2f}")   




# otra forma de pensarlo

a = float(input("Digite un valor x: "))
b = float(input("Digite otro valor x: "))

operacion = input("Digite que operacion desea realizar: ").lower()

suma = a + b
resta = a - b
multiplicacion = a * b
division = a/b

if operacion=='suma':
    print(suma)
elif operacion=='resta':
    print(resta)
elif operacion=='multiplicacion':
    print(multiplicacion)
elif operacion==division:
    print(division)