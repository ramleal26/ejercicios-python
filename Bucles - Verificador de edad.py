edad = int(input("Por favor, digite su edad: "))
i = 1

if edad >0 and edad<120:
    print(f"Edad correcta.Su edad es de: {edad} años.")

while edad<0 or edad>120 :
    print("Edad incorrecta. Usted no cumple hacia atras y probablemente no tenga mas de 120 años\nAunque uno nunca sabe") 
    i += 1 
    edad = int(input("Por favor, vuelva ingresar su edad."))
    if i == 3:
        print("Usted agoto el maximo de intentos. \nPrograma finalizado.")
        break;



    