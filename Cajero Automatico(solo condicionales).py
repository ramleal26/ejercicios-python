#Ejercicio 5: 
#Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá el siguiente menú de opciones: 
#1. Ingresar dinero en la cuenta
#2. Retirar dinero de la cuenta
#3. Mostrar dinero disponible
#4. Salir

#paso 1: especificar dinero en la cuenta
#paso 2: mostrar menu de opciones al usuario.
#paso 3: declarar condicionales.

inicial = 1000

opciones = input("Bienvenido/a a DIGITLBANK\nPor Favor digite su operacion a realizar:\na)Ingresar Dinero a la cuenta\nb)Retirar Dinero de la cuenta\nc)Mostrar Dinero Disponible\n").lower()

if opciones=='a':
 ingresodinero =float(input("Digite el monto que quiere ingresar: "))
 
 dineromostrar = ingresodinero + inicial
 
 print (f"Ahora su cuenta posee = {dineromostrar}$")

elif opciones=='b':
 
 retirardinero= float(input(f"Saldo disponible={inicial}$\nIngrese el monto que desea retirar: "))
 dineromostrarb = inicial - retirardinero
 print (f"Por favor, retire su dinero = {dineromostrarb}$")
 if retirardinero > inicial:
 print("Saldo Insuficiente, por favor repita la operacion")

elif opciones=='c':
 print(f"Su saldo disponible es = {inicial}$")

else:
    print("Valor digitado incorrecto. Por favor, vuelva a ingresar su digito.\na= Ingresar Dinero\nb= Retirar Dinero\nc=Mostrar saldo disponible")