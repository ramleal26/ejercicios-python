#Esta calculadora pide el promedio del estudiante, su cantidad de creditos y los creditos totales de su carrera.






class Calculadora():
    
    
    
    def __init__(self, tcc, presentacion):
        self.tcc = tcc
        self.presentacion = presentacion

    
    
    
    def promedio(self):
         print(self.presentacion)
         self.promedio = float(input("Digite su promedio: \n"))
  

    def tco(self):
        self.tco = int(input("Digite sus creditos obtenidos: \n"))


    def coeficiente(self):
        
        self.coeficiente = self.promedio/2 + self.tco/self.tcc * 5
        
        print(f"Su coeficiente es de:\n{self.coeficiente}\n")



calculadoratpi = Calculadora(258,"\nEsta es una calculadora hecha para obtener el coeficiente de la Tecnicatura en Programacion Informatica.\nPor favor, utilizar puntos por comas, por ejemplo:\n 6.23 o 5.67\n")


calculadoratpi.promedio()
calculadoratpi.tco()
calculadoratpi.coeficiente()










