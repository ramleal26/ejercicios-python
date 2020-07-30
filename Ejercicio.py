#Ejercio 1 / operacion arimetica. Voy a realizar una calculadora que encuentre las raices de una ecuacion cuadratica a partir de 
# los numeros digitados por el usuario.

#primero pedimos las variables

a = float(input("Digite el valor de a: "))
b = float(input("Digite el valor de b: "))
c = float(input("Digite el valor de c: "))


operacion = (a**3 *(b**2-2*a*c))/(2*b) 

print(f"el resultado de la operacion es: {operacion} ")


