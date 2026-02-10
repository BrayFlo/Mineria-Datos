#Ejercicio 1
num =5
result = num%2
if result == 0:
    print("Numero par")
else :
    print("Numero impar")




#Ejercicio 2
numero =1
if numero > 0:
    print ("El numero ingresado es positivo")
elif numero <0:
    print ("El numero ingresado es negativo")

#Ejercicio 3
edad = 18
if edad >=18:
    print ("Eres mayor de edad")
elif edad <18:
    print("No eres mayor de edad")

#Ejercicio 4:
calif = 70
if calif >=60:
    print("Estudiante aprobado")
elif calif <60:
    print("Estudiante reprobado, inicia el semestre desde 0")

#Ejercicio 5
calif = 80
if calif >=90:
    print("El alumno aprobo con A")
if calif ==80 and calif ==89:
    print("El alumno aprobo con B")
if calif ==70 and calif ==79:
    print("El alumno aprobo con C")
if calif ==60 and calif ==69:
    print("El alumno aprobo con D")
if calif <60:
    print("El alumno reprobo con F")

#Ejercicio 6
temp = 50
if temp <0:
    print("El estado de la materia es solido")
if temp ==0 and temp==100:
    print("El estado de la materia es liquido")
if temp >100:
    print("El estado de la materia es vapor")