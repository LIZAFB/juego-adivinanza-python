#JUEGO DE ADIVINANZA

import random

numeroSecreto = random.randint(1, 100)
adivinado = False # variable para asignarle True si se adivina el numero
cantidadIntentos = 0
cantidadMaximaIntentos = 5

print("Bienvenido al juego de adivinanza")
print("Estoy pensando en un numero entre 1 y 99")

while not adivinado and cantidadIntentos < cantidadMaximaIntentos:
    numero = int(input("Ingresa tu adivinanza del 0 100: "))#TODO: convertir a numero
    if numero == numeroSecreto:
        print("Felicidades, adivinaste el numero secreto")
        adivinado = True
        #la condición debe cambiar para que no vuelva a entrar al bucle
    elif numero < numeroSecreto:
        print("El numero secreto es mayor que tu adivinanza")
    else:
        print("El numero secreto es menor que tu adivinanza")
    cantidadIntentos += 1

if not cantidadIntentos < cantidadMaximaIntentos:
    print("Lo siento, has agotado tus intentos. El numero secreto era:", numeroSecreto)
    