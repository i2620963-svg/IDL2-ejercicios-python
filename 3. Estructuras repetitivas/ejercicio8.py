
# IDENTIFICACIÓN DE VARIABLES

edad = 0
sexo = ""
respuesta = ""

total_personas = 0
hombres = 0
mujeres = 0

mayores_edad = 0
menores_edad = 0

suma_edades_hombres = 0
suma_edades_mujeres = 0

promedio_hombres = 0.0
promedio_mujeres = 0.0

menor_edad = 0
mayor_edad = 0

# INGRESO DE DATOS Y PROCESO

while True:

    print("\n========== REGISTRO DE ASISTENTE ==========")

    # INGRESAR Y VALIDAR LA EDAD

    edad = int(input("Ingrese la edad: "))

    while edad <= 0:
        print("Error: La edad debe ser mayor que cero.")
        edad = int(input("Ingrese nuevamente la edad: "))

    # INGRESAR Y VALIDAR EL SEXO

    sexo = input("Ingrese el sexo (M/F): ").upper()

    while sexo != "M" and sexo != "F":
        print("Error: Ingrese M o F.")
        sexo = input("Ingrese nuevamente el sexo (M/F): ").upper()

    # CONTABILIZAR ASISTENTES

    total_personas = total_personas + 1

    # CLASIFICAR POR SEXO Y ACUMULAR EDADES

    if sexo == "M":
        hombres = hombres + 1
        suma_edades_hombres = suma_edades_hombres + edad

    else:
        mujeres = mujeres + 1
        suma_edades_mujeres = suma_edades_mujeres + edad

    # CLASIFICAR POR MAYORIA DE EDAD

    if edad >= 18:
        mayores_edad = mayores_edad + 1
    else:
        menores_edad = menores_edad + 1

    # DETERMINAR MENOR Y MAYOR EDAD

    if total_personas == 1:
        menor_edad = edad
        mayor_edad = edad

    else:

        if edad < menor_edad:
            menor_edad = edad

        if edad > mayor_edad:
            mayor_edad = edad

    # CONSULTAR SI DESEA REGISTRAR OTRA PERSONA

    respuesta = input("¿Desea registrar otra persona? (S/N): ").upper()

    while respuesta != "S" and respuesta != "N":
        print("Error: Ingrese S o N.")
        respuesta = input("¿Desea registrar otra persona? (S/N): ").upper()

    if respuesta == "N":
        break

# CÁLCULO DE PROMEDIOS

if hombres > 0:
    promedio_hombres = suma_edades_hombres / hombres

if mujeres > 0:
    promedio_mujeres = suma_edades_mujeres / mujeres

# SALIDA DE DATOS

print("\n========== RESULTADOS DE LA FIESTA ==========")

print("Total de personas:", total_personas)

print("\nCANTIDAD POR SEXO")
print("Hombres:", hombres)
print("Mujeres:", mujeres)

print("\nCLASIFICACIÓN POR EDAD")
print("Mayores de edad (18 años o más):", mayores_edad)
print("Menores de edad (menos de 18 años):", menores_edad)

print("\nPROMEDIO DE EDADES")

if hombres > 0:
    print("Promedio de hombres:", round(promedio_hombres, 2))
else:
    print("No se registraron hombres.")

if mujeres > 0:
    print("Promedio de mujeres:", round(promedio_mujeres, 2))
else:
    print("No se registraron mujeres.")

print("\nEDADES EXTREMAS")
print("Menor edad registrada:", menor_edad)
print("Mayor edad registrada:", mayor_edad)