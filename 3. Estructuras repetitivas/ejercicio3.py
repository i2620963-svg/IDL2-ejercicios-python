while True:
    # IDENTIFICACIÓN DE VARIABLES

    n = 0
    numero = 0.0
    x = 0.0
    i = 0

    menores = 0
    mayores = 0
    iguales = 0
    comprendidos = 0
    ninguna = 0

    p_menores = 0.0
    p_mayores = 0.0
    p_iguales = 0.0
    p_comprendidos = 0.0
    p_ninguna = 0.0

    # INGRESO DE DATOS

    n = int(input("Ingrese la cantidad de números: "))

    x = float(input("Ingrese el número X (mayor o igual a 1): "))

    # PROCESO

    if n > 0 and x >= 1:

        for i in range(1, n + 1):

            numero = float(input("Ingrese un número: "))

            if numero < x:
                if numero >= 1:
                    comprendidos = comprendidos + 1
                else:
                    menores = menores + 1

            elif numero > x:
                mayores = mayores + 1

            elif numero == x:
                iguales = iguales + 1

            else:
                ninguna = ninguna + 1

        # CÁLCULO DE PORCENTAJES

        p_menores = menores / n * 100
        p_mayores = mayores / n * 100
        p_iguales = iguales / n * 100
        p_comprendidos = comprendidos / n * 100
        p_ninguna = ninguna / n * 100

        # SALIDA DE DATOS

        print("======= RESULTADOS =======")

        print("Porcentaje de menores que X:",
            p_menores, "%")

        print("Porcentaje de mayores que X:",
            p_mayores, "%")

        print("Porcentaje de iguales a X:",
            p_iguales, "%")

        print("Porcentaje comprendidos entre 1 y X:",
            p_comprendidos, "%")

        print("Porcentaje que no cumple ninguna condición:",
            p_ninguna, "%")

    else:
        print("Error: N debe ser mayor que cero y X debe ser mayor o igual a 1.")
