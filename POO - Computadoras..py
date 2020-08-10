
class Computadora(): #estado inicial - propiedades # por convencion siempre se utilizan las primeras letras en mayusculas. Ejemplo: MiComputadoraPersonal
    
    def __init__(self):
            
        self.ram = 8
        self.hdd = 1000 # todas nuestras computadoras tendran 1000 GB de HDD
        self.cpu = 2.4
        self.encendido = True
        self.internet = True



# comportamientos
   
    def prender(self,presionarboton):
        
        self.encendido = presionarboton
        
        if presionarboton == True:
            
            return "Esta encendida."
        
        else:
            
            return "la computadora esta apagada."
    
    def conectividad(self,conectado):
        
        self.internet = conectado

        if conectado == True:
            
            return "La computadora tiene internet."
        
        else:
            
            return "No tiene conexion a internet."
    
    def nowifi(self):
        self.internet = False
    
    
    def wifi(self):
        if self.internet:
            
            return "La computadora tiene el Wi fi activado."
        
        else:
            
            return "La computadora esta con el wi fi desactivado."





#Computadora 1

computadora1 = Computadora()

print(f"La ram de la computadora es de: {computadora1.ram}GB")
print(f"La cpu de la computadora es de: {computadora1.cpu} GHZ")
print(computadora1.prender(True))
print(computadora1.conectividad(True))
print(computadora1.wifi())


print("________________________________________________________________\n")

#computadora 2 

computadora2 = Computadora()

computadora2.ram = 16
computadora2.cpu = 1.8
computadora2.hdd = 2000
print(f"La ram de la computadora es de: {computadora2.ram}GB")
print(f"La cpu de la computadora es de: {computadora2.cpu} GHZ")
print(f"El HDD de la computadora es de: {computadora2.hdd} TB")
print(computadora1.prender(False))
print(computadora1.conectividad(False))
computadora2.nowifi()
print(computadora2.wifi())