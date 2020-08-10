# verificacion de edad - metodo 1:

#edad = int(input("Digite su edad: "))

#if edad>=0 and edad<120: #primero se corrobora que la edad sea mayor a 0 y menor a 120
    #if edad >= 18: #despues que sea mayor a 18  

          #print("Usted es mayor de edad") # con el condicional anidado podemos hacer mas de una pregunta, que verique los datos del usuario.

#elif edad>120 or edad < 0:
    #print("Edad incorrecta")


#else:
     #print("Usted es menor de edad.")'

#metodo 2 - seguimos el modelo de la notacion constructiva.

edad = int(input("Digite su edad: "))

if  0<edad<100 and edad>=18:

    print("usted es mayor de edad")

elif 0<edad<18:

    print("usted es menor de edad.")


else:

 print("Edad Incorrecta")