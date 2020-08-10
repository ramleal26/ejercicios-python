

a = input("Digite su email: ")

if (a =="@" and a =="."): 
       print("mail correcto")
elif (a =="@" and a ==".") and (a == "-" and a== "_"):
    print("mail correcto")
else:
    print("Mail invalido. Recuerde utilizar los caracteres '@','-','.''_' " )
 