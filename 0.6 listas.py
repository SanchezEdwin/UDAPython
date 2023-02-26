import time,os,winsound
#Funcion de Arreglos
print("Bienvenido, elimine el que no sea un superheroe")
juego2=["[0] Spiderman","[1] Venom","[2] Daredevil","[3] Iron Fist"]
print(juego2)
i=int(input())
juego2.pop(i)
print(juego2)
time.sleep(3)
os.system('cls')
if i == 1:
    print("Felicidades. A eliminado al impostor exitosamente")
    winsound.Beep(3500,100)
    winsound.Beep(5000,100)
elif i != 1:
    print("Oh no. El impostor no fue eliminado y los heroes han perdido por su culpa :(")
    print(juego2)
    winsound.Beep(3500,100)
    winsound.Beep(2500,1500)
time.sleep(3)
os.system('cls')
print("Ahora en lugar de eliminar, reemplaza al impostor. Primero selecciona un personaje")
juego2 = ["[0] Spiderman","[1] Venom","[2] Daredevil","[3] Iron Fist"]
print(juego2)
i=int(input())
print("Ahora escribe el personaje que quieras")
j=input()
juego2[i]=f"[{i}] {j}"
print(juego2)

