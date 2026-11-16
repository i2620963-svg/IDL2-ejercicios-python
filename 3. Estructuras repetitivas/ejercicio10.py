# IDENTIFICACIÓN DE VARIABLES

n = 0
nota = 0.0
i = 0

notas = []

mayor = 0.0
menor = 0.0

cant_mayor = 0
cant_menor = 0

suma = 0.0
promedio = 0.0

pares = 0
impares = 0

aprobados = 0
desaprobados = 0

p_aprobados = 0.0
p_desaprobados = 0.0

# INGRESO Y VALIDACIÓN DE LA CANTIDAD DE ESTUDIANTES

while True:

    n = int(input("Ingrese la cantidad de estudiantes (5-20): "))

    if n >= 5 and n <= 20:
        break
    else:
        print("Error: Ingrese una cantidad entre 5 y 20.")

# INGRESO Y VALIDACIÓN DE LAS NOTAS

for i in range(1, n + 1):

    print("\nEstudiante", i, "de", n)

    while True:

        nota = float(input("Ingrese la nota (0-20): "))

        if nota >= 0 and nota <= 20:
            break
        else:
            print("Error: La nota debe estar entre 0 y 20.")

    # ALMACENAR LA NOTA EN LA LISTA

    notas.append(nota)

    # ACUMULAR LAS NOTAS

    suma = suma + nota

# PROCESO

# DETERMINAR LA MAYOR Y MENOR NOTA

mayor = max(notas)
menor = min(notas)

# CONTAR CUANTOS OBTUVIERON LA MAYOR Y MENOR NOTA

cant_mayor = notas.count(mayor)
cant_menor = notas.count(menor)

# CALCULAR EL PROMEDIO

promedio = suma / n

# CLASIFICAR LAS NOTAS

for nota in notas:

    # CONTAR NOTAS PARES E IMPARES

    if nota.is_integer():

        if int(nota) % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1

    # CLASIFICAR APROBADOS Y DESAPROBADOS

    if nota >= 13:
        aprobados = aprobados + 1
    else:
        desaprobados = desaprobados + 1

# CALCULAR LOS PORCENTAJES

p_aprobados = (aprobados / n) * 100

p_desaprobados = (desaprobados / n) * 100

# SALIDA DE DATOS

print("\n========== RESULTADOS DEL CURSO ==========")

print("\nNOTAS REGISTRADAS:")
print(notas)

print("\nRESULTADOS GENERALES")
print("Cantidad de estudiantes:", n)
print("Mayor nota:", mayor)
print("Menor nota:", menor)

print("\nCANTIDAD DE NOTAS EXTREMAS")
print("Estudiantes con la mayor nota:", cant_mayor)
print("Estudiantes con la menor nota:", cant_menor)

print("\nPROMEDIO DEL SALÓN")
print("Promedio de notas:", round(promedio, 2))

print("\nCLASIFICACIÓN DE NOTAS")
print("Notas pares:", pares)
print("Notas impares:", impares)

print("\nRESULTADOS ACADÉMICOS")
print("Alumnos aprobados:", aprobados)
print("Alumnos desaprobados:", desaprobados)

print("\nPORCENTAJES")
print("Porcentaje de aprobados:", round(p_aprobados, 2), "%")
print("Porcentaje de desaprobados:", round(p_desaprobados, 2), "%")