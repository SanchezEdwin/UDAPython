import time,os

lenguajes=['Python','C','C#','C++','VB','VBA','JavaScript','Java']
respuestas=[]
print("Selecciona los lenguajes que sepas")
i=0
for lenguaje in lenguajes:
    print(f"[{i}]{lenguaje}")
    i=i+1
for respuesta in respuestas:
    respuesta=int(input())
for respuesta in respuestas:
    print(respuesta)
i=0
print("Usted conoce")
for lenguaje in lenguajes:
    i=i+1

#Programa 3 faltas reprobado si tienes adeudo es falta si tienes todo pagado no hay falta