
# IDENTIFICACIÓN DE VARIABLES

n = 0
numero = 0.0
contador = 0

maximo = 0.0
minimo = 0.0

# INGRESO DE DATOS

n = int(input("Ingrese la cantidad de números: "))

# PROCESO

if n > 0:

    while True:

        # MOSTRAR EL AVANCE DEL INGRESO

        print("\nNúmero", contador + 1, "de", n)

        numero = float(input("Ingrese un número: "))

        contador = contador + 1

        # INICIALIZAR MAXIMO Y MINIMO

        if contador == 1:
            maximo = numero
            minimo = numero

        else:

            # DETERMINAR EL MAXIMO

            if numero > maximo:
                maximo = numero

            # DETERMINAR EL MINIMO

            if numero < minimo:
                minimo = numero

        # MOSTRAR CUANTOS NUMEROS FALTAN

        print("Números ingresados:", contador)
        print("Números pendientes:", n - contador)

        # VERIFICAR SI SE INGRESARON LOS N NUMEROS

        if contador == n:
            break

    # SALIDA DE DATOS

    print("\n======= RESULTADOS =======")
    print("Cantidad de números ingresados:", contador)
    print("Número máximo:", maximo)
    print("Número mínimo:", minimo)

else:
    print("Error: La cantidad de números debe ser mayor que cero.")