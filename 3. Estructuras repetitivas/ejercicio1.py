while True:
    # IDENTIFICACIÓN DE VARIABLES
    n = 0
    i = 0

    suma_pares = 0
    suma_impares = 0

    contador_pares = 0
    contador_impares = 0

    promedio_pares = 0.0
    promedio_impares = 0.0

    # INGRESO DE DATOS
    n = int(input("Ingrese el número limite N: "))

    # PROCESO
    for i in range(1, n + 1):

        if i % 2 == 0:
            suma_pares = suma_pares + i
            contador_pares = contador_pares + 1

        else:
            suma_impares = suma_impares + i
            contador_impares = contador_impares + 1

    # CÁLCULO DE PROMEDIOS
    if contador_pares > 0:
        promedio_pares = suma_pares / contador_pares

    if contador_impares > 0:
        promedio_impares = suma_impares / contador_impares

    # SALIDA DE DATOS
    print("======= RESULTADOS =======")

    print("SUMA Y PROMEDIO DE PARES")
    print("Suma de pares:", suma_pares)
    print("Cantidad de pares:", contador_pares)

    if contador_pares > 0:
        print("Promedio de pares:", promedio_pares)
    else:
        print("No existen números pares.")

    print("--------------------------")

    print("SUMA Y PROMEDIO DE IMPARES")
    print("Suma de impares:", suma_impares)
    print("Cantidad de impares:", contador_impares)

    if contador_impares > 0:
        print("Promedio de impares:", promedio_impares)
    else:
        print("No existen números impares.")