import time,os
os.system('cls')
#Funcion sin parametro
def Venom():
    print("Venom es un antiheroe actualmente en los comics")
Venom()

#Funcion con parametro
def Spiderman(Heroe):
    print(f"{Heroe} es mi superheroe favorito")
Spiderman("Spiderman")

#Funcion con parametro multiple
def HeroesFuertes(Heroe1,Heroe2):
    print(f"{Heroe1} y {Heroe2} son muy poderosos")
HeroesFuertes("Thor","Hulk")
time.sleep(5)

os.system('cls')
#Funcion captura tu nombre y tu puesto de trabajo
def funcion(nombre,puesto):
    print(f"Su nombre es {nombre} y es {puesto}")
    time.sleep(2.5)
print("Teclee su nombre")
nombre = input()

print("Teclee su puesto")
puesto = input()
funcion(nombre,puesto)

os.system('cls')
#Funcion Minijuego de Adivinar el Numero
import random

def juego(adivinado,real):
    if adivinado == real:
        print("Usted gana")
        time.sleep(2)

real = random.randrange(1,10)
adivinado=0
while adivinado!=real:
    print("Teclee un numero")
    adivinado = int(input())
    if adivinado==real:
        break
juego(adivinado,real)

os.system('cls')
#Funcion calculadora
def calculadora(opcion,numero1,numero2):
    if opcion == 1:
        print(f"{numero1}+{numero2} es igual a",numero1+numero2)
        time.sleep(2)
    elif opcion == 2:
            print(f"{numero1}-{numero2} es igual a",numero1-numero2)
            time.sleep(2)
print("Bienvenido a la calculadora de Python. Presione 1 para Sumar y 2 para Restar")
opcion= int(input())
print("Teclee el primer numero")
numero1= int(input())
print("Teclee el segundo numero")
numero2= int(input())
calculadora(opcion,numero1,numero2)
print("By: Edwin Sanchez")
time.sleep(2)
os.system('cls')