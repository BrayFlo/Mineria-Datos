from coches import Coche

mi_coche = Coche()

# 2. Pedir aumento de velocidad por teclado
print("---- Informacion general del automovil ----")
aumento = float(input("¿Cuántos km/h quieres aumentar?: "))
mi_coche.acelerar_velocidad(aumento)

# 3. Pedir disminución de velocidad por teclado
decremento = float(input("¿Cuántos km/h quieres disminuir?: "))
mi_coche.frenar_velocidad(decremento)

#Mostramos la informavion final del automovil
mi_coche.mostrar_info()
