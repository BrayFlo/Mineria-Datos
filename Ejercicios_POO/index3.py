from bancos import Banco

mi_banco = Banco()

# 2. Abonos a la cuenta bancaria
abono = float(input("¿Desea depositar?: "))
mi_banco.depositar(abono)

# 3. Cargos a la cuenta bancaria
cargo = float(input("¿Cuanto desea retirar?: "))
mi_banco.retirar(cargo)

#Mostramos la informavion final del automovil
mi_banco.mostrar_info()

