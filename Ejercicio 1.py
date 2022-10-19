#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en
# líneas distintas el nombre del usuario tantas veces como el número introducido.

nombreUsuario = input("Introduce tu nombre")
numeroEntero = input("Introduce el numero de veces que se quiera repetir tu nombre")

print((nombreUsuario + "\n") * int(numeroEntero))