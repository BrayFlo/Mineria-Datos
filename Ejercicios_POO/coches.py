#Bryan Hernández Flores
#Ejercicio 1: Crear un clase llamada coche

class Coche:
    #Atributos
    def __init__(self):
        self.marca = "Mazda"
        self.modelo ="Mazda 3"
        self.color = "Negro"
        self.velocidad = 0
    
    #Metodos

    def acelerar_velocidad(self, cantidad):
        self.velocidad += cantidad
        print(f"La velocidad del automovil ha aumentado a: {cantidad} km/h. Velocidad total acumulada: {self.velocidad} km/h")
    
    def frenar_velocidad(self, cantidad):
        if self.velocidad - cantidad < 0:
            self.velocidad = 0
            print(f"El automovil no registra velocidad acumulada 0 km/h")
        else:
            self.velocidad -= cantidad
            print(f"La velocidad del automovil ha disminuido {cantidad} km/h. Velocidad total acumulada: {self.velocidad} km/h")
    
    def mostrar_info(self):
        print(f"---- Informacion del Automovil ----")
        print(f"La marca del automovil es: {self.marca}")
        print(f"El modelo del automovil es de: {self.modelo}")
        print(f"El color del automovil es de: {self.color}")
        print(f"La velocidad actual del automovil es de: {self.velocidad} km/h")
