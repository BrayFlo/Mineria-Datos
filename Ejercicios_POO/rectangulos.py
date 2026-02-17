#Bryan Hernández Flores
#Ejercicio 3: Crear una clase llamada Rectangulo
class Rectangulo:
    #Definición de Atributos
    def __init__(self):
        self.ancho = float(input("Ingresa el ancho del rectangulo: "))
        self.alto = float(input("Ingresa el alto del rectangulo: "))
    
    #Definición de Métodos

    def calcular_area(self):
        return self.ancho * self.alto
    
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

    def mostrar_info(self):
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        print(f"---- Informacion del rectangulo ----")
        print(f"El ancho del rectangulo es de: {self.ancho} cm.")
        print(f"El alto del rectangulo es de: {self.alto} cm.")
        print(f"El area del rectangulo es de: {area} cm cuadrados.")
        print(f"El ancho del rectangulo es de: {perimetro} cm.")
        
