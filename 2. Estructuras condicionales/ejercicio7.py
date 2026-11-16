# IDENTIFICACIÓN DE VARIABLES
hora = 0
minuto = 0
segundo = 0
n = 0

total_segundos = 0
hora_final = 0
minuto_final = 0
segundo_final = 0

# INGRESO DE DATOS
hora = int(input("Ingrese la hora (HH): "))
minuto = int(input("Ingrese los minutos (MM): "))
segundo = int(input("Ingrese los segundos (SS): "))
n = int(input("Ingrese la cantidad de segundos a agregar: "))

# PROCESO

# Validar los datos ingresados
if hora < 0 or hora > 23 or minuto < 0 or minuto > 59 or segundo < 0 or segundo > 59 or n < 0:
    print("Error: Los datos ingresados no son válidos.")

else:
    # Convertir la hora inicial a segundos
    total_segundos = (hora * 3600) + (minuto * 60) + segundo

    # Agregar los segundos
    total_segundos = total_segundos + n

    # Calcular la hora, minutos y segundos finales
    hora_final = (total_segundos // 3600) % 24
    minuto_final = (total_segundos % 3600) // 60
    segundo_final = total_segundos % 60

    # SALIDA DE DATOS
    print("========== HORA RESULTANTE ==========")
    print("La hora después de", n, "segundos es:")
    print(f"{hora_final:02d}:{minuto_final:02d}:{segundo_final:02d}")