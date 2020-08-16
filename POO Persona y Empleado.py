class Persona():

    def __init__(self, nombre, edad, estatura, peso):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.peso = peso

    def descripcion(self):
        
        print(f"\n Nombre: {self.nombre}\n", f"Edad: {self.edad}\n", f"Estatura: {self.estatura}\n", f"Peso: {self.peso}\n")


Fernando = Persona("Fernando","53 años", "1.70 cm", "64 kg")


print("\nDescripcion de Fernando")

Fernando.descripcion()

 

class Empleado(Persona):

   
    def __init__(self, nombre_empleado, trabajo, salario, edad_empleado, estatura_empleado, peso_empleado):
        
        super().__init__(nombre_empleado, edad_empleado , estatura_empleado, peso_empleado)#con la funcion super() hacemos un llamado a el constructor de la clase padre.
        
        self.salario = salario
        self.trabajo = trabajo

    def descripcion(self):
        super().descripcion()
        
        print(f"Salario:{self.salario}",f"\nTrabaja de:{self.trabajo}")





Ricardo = Empleado("Richard", "Programador", "50.000", "55", "1.79", "80 KG")



Ricardo.descripcion()














