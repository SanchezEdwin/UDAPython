def comprobar(faltas,adeudo,clase,nombre):
    status=["Aprobado","Reprobado"]
    if adeudo == "Si":
        faltas = faltas+1
    if faltas >= 3:
        status = "Reprobado"
    if faltas < 3:
        status = "Aprobado"
    print(f"En la clase {clase} el alumno {nombre} se encuentra {status} con {faltas} faltas")

print ("Por favor escriba su nombre")
nombre=input()

print (f"Bienvenido {nombre}. Por favor escriba la clase a consultar")
clase=input()

print ("¿Debe algun pago escolar?")
adeudo=input()

print ("¿Cuantas veces a faltado en este periodo?")
faltas=int(input())

comprobar(faltas,adeudo,clase,nombre)