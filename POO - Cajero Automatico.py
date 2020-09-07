#1) Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad (puede tener decimales).
#El titular será obligatorio y la cantidad es opcional. Crea dos constructores que cumpla lo anterior.
#Tendrá dos métodos especiales:
#ingresar(double cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, se 
#retirar(double cantidad): se retira una cantidad a la cuenta, si restando la cantidad actual a la que nos pasan es negativa, la cantidad de la cuenta pasa a ser 0.



class Cuenta():
    
    def __init__(self):

        self.nombre = "Digital Bank"
        self.cantidadinicial = 2000





    def titularingreso(self):
        
        titularingreso2 = input("Por favor, ingrese su nombre: ")
        
        print(f"Hola, {titularingreso2}!")




    def operacion(self):   

        self.operacion = input("\nDigite su operacion \na.Ingreso \nb.Egreso:\n ").lower()
        
        while self.operacion!= "a" and self.operacion !="b":
            
            print("Error.\nVuelva a digitar la operacion \nValores permitidos: letras a y b.\n")
            
            self.operacion = input("Digite su operacion \na.Ingreso \nb.Egreso:\n ")



    def ingresoegreso(self):
    
#OPCION A - ingreso de dinero


        if self.operacion == "a":

         self.monto = float(input("\nDigite el monto a ingresar: "))
         print(f"Su monto es de: {self.monto+self.cantidadinicial}$")

        #si el monton ingresado es negativo, repetir pregunta 
         while self.monto<0:
          
          print("No se permiten valores negativos, vuelva a digitar su monto(solo valores positivos).")
          self.monto = float(input("Digite el monto a ingresar:\n"))
         
          if self.monto>0:
            print(f"Su saldo actual es de: {self.monto+self.cantidadinicial}U$$")


#OPCION B - egreso de dinero

    
        elif self.operacion == "b":
        
         self.monto2 = float(input("Ingrese el monto a retirar: "))


#cuando el monto de egreso es positivo, entonces:        



         if self.monto2>0:
            
            self.resultante = self.cantidadinicial - self.monto2
            
            #si el resultado es mayor a 0, entonces imprimir resultante
            if resultante>0: 
             print(f"Su dinero restante es de: {resultante}U$$")
            
            #si el resultado es menor a 0, no imprimir el mismo, sino que el saldo restante sera 0

            elif resultante<0:
                print("su saldo es de: 0.0 U$$")
         

#cuando el monto2 de egreso sea un valor negativo, entonces:

         while self.monto2<0:
          
          print("No se permiten valores negativos, vuelva a digitar su monto.")
          self.monto = float(input("Digite el monto a ingresar: \n"))
         
         if self.monto2>0:
            
            self.resultante = self.cantidadinicial - self.monto2

            print(f"Su dinero restante es de: {self.resultante}$")
         

             
            
        

             


   

#programa 

micuenta = Cuenta()

micuenta.titularingreso()
micuenta.operacion()
micuenta.ingresoegreso()


