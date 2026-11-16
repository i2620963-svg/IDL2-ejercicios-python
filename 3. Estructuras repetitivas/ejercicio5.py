# IDENTIFICACIÓN DE VARIABLES

mes = 0
deposito = 0.0
ahorro = 0.0

# INGRESO DE DATOS Y PROCESO

while True:

    # MOSTRAR EL MES DEL DEPOSITO

    mes = mes + 1

    print("\n========== MES", mes, "==========")

    deposito = float(input("Ingrese el monto del depósito: S/ "))

    # VALIDAR QUE EL DEPOSITO NO SEA NEGATIVO

    if deposito >= 0:

        # CALCULAR EL AHORRO ACUMULADO

        ahorro = ahorro + deposito

        # MOSTRAR EL AVANCE DEL AHORRO

        print("Mes:", mes)
        print("Depósito realizado: S/", deposito)
        print("Ahorro acumulado: S/", ahorro)

    else:

        print("Error: El depósito no puede ser negativo.")

        mes = mes - 1

    # VERIFICAR SI SE COMPLETARON LOS 12 MESES

    if mes == 12:
        break

# SALIDA DE DATOS

print("\n======= RESUMEN ANUAL =======")
print("Meses registrados:", mes)
print("Ahorro final del año: S/", ahorro)