#Bryan Hernández Flores
#Ejercicio 2: Crear una clase llamada Cuenta Bancaria

class Banco:
    #Atributos
    def __init__(self):
        self.titular = "Bryan Hernandez Flores"
        self.saldo = 0.0

    #Metodos
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso de: ${cantidad}")
            print(f"Saldo total: ${self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")
            
    def retirar(self, cantidad):
        # Si no hay dinero suficiente, NO restamos nada
        if cantidad > self.saldo:
            print(f"Error: Fondos insuficientes. Tu saldo actual es de: ${self.saldo}")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso por: ${cantidad}")
            print(f"Nuevo saldo disponible: ${self.saldo}")
    
    def mostrar_info(self):
        print(f"---- Informacion de la cuenta bancaria ----")
        print(f"Titular: {self.titular}")
        print(f"El saldo total de la cuenta es: ${self.saldo}")

