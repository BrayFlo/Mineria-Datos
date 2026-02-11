#Ejercicio 1
n=int(input("Introduce un numero hasta donde quieres sumar:"))
sum=0
for i in range (1, n+1):
    sum = sum +i
print(f"La suma de los primeros {n} numeros es de: {sum}")

#Ejercicio 2
n=int(input("Introduce un numero para determinar su factorial:"))
factorial=1
for i in range (1, n + 1):
    factorial = factorial *i
print(f"El factorial de {n} numeros es: {factorial}")

#Ejercicio 3
tabla_del = int(input("¿De que numero quieres la tabla? "))

print(f"--- Tabla del {tabla_del} ---")

for i in range(1, 11, 1):
    resultado = tabla_del * i
    print(f"{tabla_del} x {i} = {resultado}")

#Ejercicio 4
sum_notas=0
cont_notas=0

for i in range (1000):
    nota= float(input("Ingresa una nota (o un numero negativo para terminar): "))

    if nota <0:
        break
    sum_notas += nota
    cont_notas +=1

if cont_notas >0:
    promedio = sum_notas / cont_notas
    print(f"El promedio de las {cont_notas} notas es: {promedio:.2 f}")
else:
    print("No se ingresaron notas válidas.")

#Ejercicio 5
base = int(input("Base: "))
exponente = int(input("Exponente: "))

resultado = 1

for _ in range(exponente):
    resultado *= base

print(f"{base} elevado a la {exponente} es: {resultado}")

#Ejercicio 6
a = int(input("Valor inicial (A): "))
b = int(input("Valor final (B): "))

suma_pares = 0

for num in range(a, b + 1):
    
    if num % 2 == 0:
        suma_pares += num

print(f"La suma de los pares entre {a} y {b} es: {suma_pares}")