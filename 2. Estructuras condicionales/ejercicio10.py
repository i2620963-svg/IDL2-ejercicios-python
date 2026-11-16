
# IDENTIFICACIÓN DE VARIABLES
codigo = 0
minutos = 0
zona = ""
costo_minuto = 0.0
total = 0.0

# INGRESO DE DATOS
codigo = int(input("Ingrese el código de la zona: "))
minutos = int(input("Ingrese la cantidad de minutos hablados: "))

# PROCESO
if minutos <= 0:
    print("Error: La cantidad de minutos debe ser mayor que cero.")

elif codigo == 10:
    zona = "América del Norte"
    costo_minuto = 2.20

elif codigo == 12:
    zona = "América del Centro"
    costo_minuto = 2.50

elif codigo == 20:
    zona = "América del Sur"
    costo_minuto = 1.20

elif codigo == 22:
    zona = "Asia"
    costo_minuto = 3.50

elif codigo == 30:
    zona = "Europa"
    costo_minuto = 3.00

elif codigo == 32:
    zona = "África"
    costo_minuto = 3.20

else:
    print("Error: El código de zona ingresado no existe.")

# SALIDA DE DATOS
if minutos > 0 and costo_minuto > 0:
    total = minutos * costo_minuto

    print("========== DETALLE DE LLAMADA ==========")
    print("Zona geográfica:", zona)
    print("Cantidad de minutos:", minutos)
    print("Costo por minuto: S/", costo_minuto)
    print("Total a pagar: S/", round(total, 2))