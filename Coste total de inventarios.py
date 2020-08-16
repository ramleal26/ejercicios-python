#fabrica tecnologica.


class Smarts():
    def __init__(self, nombre, costo, costofinal):
        
        self.nombre = nombre
        self.corriente = True
        self.pantalla = "Color Full HD"
        self.conectividad = True
        self.multimedia = True
        self.costo = costo
        self.costofinal = costofinal
    
    def mensajes(self):
        
        if conectividad:
            return "Envia mensajes ya que posee internet."
        else:
            return "No posee conectividad y por lo tanto no envia mensajes."

    def socialmedia(self):
        
        if multimedia:
            return "Puede reproducir contenido de cualquier red social." 
        else:
            return "No reproduce contenido audiovisual y por lo tanto no es posible utilizar las redes sociales."
    
    
    def descripcion(self):
        print (f"\nNombre: {self.nombre}",f"\nCorriente: {self.corriente}", f"\nPantalla: {self.pantalla}", 
        f"\nConectividad: {self.conectividad}", f"\nSocialMedia: {self.multimedia}", f"\nCosto: {self.costo}", f"\nCosto Final: {self.costofinal}")


class Computadora(Smarts):
    def __init__(self,nombre_computadora, costo_computadora, costofinal_computadora):
        super().__init__(nombre_computadora, costo_computadora, costofinal_computadora)
        self.cpu = "I9"
        self.ram = "16 GB"
        self.disco = "SSD 240 GB"

    def descripcionPC(self):
        super().descripcion()

        print(f"Cpu:{self.cpu}", f"\nMemoria Ram:{self.ram}", f"\nDisco: {self.disco}")

#objeto computadora.
potentiarg = Computadora("Potenti-arg", "70.000 pesos", "90.000 pesos")



class Celular(Smarts):
    
    def __init__(self, nombre_celular, costo_celular, costofinal_celular):
        super().__init__(nombre_celular, costo_celular, costofinal_celular)
        self.llamadas = True
        self.antena = True
        self.memoria = "128GB"
        self.microram = "8GB"
    
    def descripcionCel(self):
        super().descripcion()
        print(f"\nAntena: {self.antena}",f"\nLlamadas:{self.llamadas}", f"\nMemoria: {self.memoria}",f"\nMemoria Ram:{self.microram}")

#objeto celular
celarg = Celular("Celarg", 40.000, 50.000)


class TvSmart(Smarts):
    
    def __init__(self, nombre_tv, costo_tv, costofinal_tv):
        super().__init__(nombre_tv, costo_tv, costofinal_tv)
        self.llamadastv = False
        self.antenatv = True
        self.memoriatv = "1GB"
        self.microramtv = "512MB"
    
    def descripcionTV(self):
        super().descripcion()
        print(f"\nAntena: {self.antenatv}",f"\nLlamadas:{self.llamadastv}", f"\nMemoria: {self.memoriatv}",f"\nMemoria Ram:{self.microramtv}")


#objeto TV

smartarg = TvSmart("Smartarg", 35.000, 50.000)

#_________________________________________________________________



#lista inventario Smarts

inventario = [potentiarg, celarg, smartarg]

print(inventario)



