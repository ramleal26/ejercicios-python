
class Celulares():

    def __init__(self, modelo):
        self.marca= "Digitarg"
        self.material = "Aluminio"
        self.maximogrosor = 0.5
        self.color = "white"
        self.conectividad = True
        self.pantallacolor = True
        self.bateria = True
    
    def mensajes(self):
 
        if self.conectividad:
            return "El celular puede enviar mensajes."
        
        else:
            return " el celular no puede enviar mensajes. Active su conectividad"
    
    def encender(self):
      
        
        if self.bateria:
            return "El celular esta encendido"
        else:
            return "El celular esta apagado"


class CelularDeEntrada(Celulares): #aqui hacemos una herencia. Nuestra primera clase es el lineamiento general de los celulares de fabrica, pero sabemos que hay distintos tipos y modelos. En este caso hacemos una sub-clase para los ceulares de gama baja/entrada
        pass

Celulareconomico = CelularDeEntrada("Entry Model")


#celular Economico, caracteristicas:

Celulareconomico.color= "Black"

print(f"La gama baja de nuestros celulares es el: \nEntry Model")
print(f"La marca es: {Celulareconomico.marca}")
print(f"Su color es: {Celulareconomico.color}")
print(f"Envia mensajes? {Celulareconomico.mensajes()}")
print(f"Esta encendido o apagado?:{Celulareconomico.encender()}")

print("_______________________________\n")
Celulareconomico.color= "White"
Celulareconomico.bateria = False

print("Celular 2")
print(f"La marca es: {Celulareconomico.marca}")
print(f"Su color es: {Celulareconomico.color}")
print(f"Envia mensajes? {Celulareconomico.mensajes()}")
print(f"Esta encendido o apagado?:{Celulareconomico.encender()} \n")



        

