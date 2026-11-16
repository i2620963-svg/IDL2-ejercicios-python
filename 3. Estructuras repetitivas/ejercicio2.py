while True:
    # IDENTIFICACIÓN DE VARIABLES
    numero = 0
    i = 0

    pares = 0
    impares = 0
    positivos = 0
    neutros = 0
    negativos = 0

    # INGRESO DE DATOS Y PROCESO
    for i in range(1, 11):

        numero = int(input(f"Ingrese el número {i} de 10: "))

        # EVALUAR SI ES PAR O IMPAR
        if numero % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1

        # EVALUAR SI ES POSITIVO, NEUTRO O NEGATIVO
        if numero > 0:
            positivos = positivos + 1
        elif numero == 0:
            neutros = neutros + 1
        else:
            negativos = negativos + 1

    # SALIDA DE DATOS
    print("\n======= RESULTADOS =======")
    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)
    print("Cantidad de números positivos:", positivos)
    print("Cantidad de números neutros:", neutros)
    print("Cantidad de números negativos:", negativos)

    # OPCIÓN PARA SALIR DEL BUCLE
    continuar = input("\n¿Desea ingresar otros 10 números? (s/n): ")
    if continuar.lower() != "s":
        print("Programa finalizado.")
        break