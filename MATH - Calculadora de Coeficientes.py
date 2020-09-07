#Esta calculadora pide el promedio del estudiante, su cantidad de creditos y los creditos totales de su carrera.


class Calculadora():
    
    
    
    def __init__(self, tcc):
        self.tcc = tcc
    
    
    def promedio(self):

         self.promedio = float(input("Digite su promedio: \n")).replace(".",",")
  

    def tco(self):
        self.tco = int(input("Digite sus creditos obtenidos: \n"))


    def coeficiente(self):
        
        self.coeficiente = self.promedio/2 + self.tco/self.tcc * 5
        
        print(f"Su coeficiente es de:\n{self.coeficiente}\n")



calculadoratpi = Calculadora(258)


calculadoratpi.promedio()
calculadoratpi.tco()
calculadoratpi.coeficiente()










