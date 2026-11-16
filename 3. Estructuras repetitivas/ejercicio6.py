# IDENTIFICACIÓN DE VARIABLES

horas = 0
minutos = 0
segundos = 0
contador = 0

# INGRESO DE DATOS

limite = int(input("Ingrese el tiempo del cronómetro en segundos: "))

# PROCESO

if limite > 0:

    while True:

        segundos = segundos + 1
        contador = contador + 1

        # CONTROLAR LOS SEGUNDOS

        if segundos == 60:
            segundos = 0
            minutos = minutos + 1

        # CONTROLAR LOS MINUTOS

        if minutos == 60:
            minutos = 0
            horas = horas + 1

        # MOSTRAR EL CRONOMETRO

        print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

        # VERIFICAR EL TIEMPO ESTABLECIDO

        if contador == limite:
            break

    # SALIDA DE DATOS

    print("======= CRONOMETRO FINALIZADO =======")
    print(f"Tiempo transcurrido: {horas:02d}:{minutos:02d}:{segundos:02d}")

else:

    print("Error: Ingrese un tiempo mayor que cero.")