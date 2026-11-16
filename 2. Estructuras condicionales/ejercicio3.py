# IDENTIFICACIÓN DE VARIABLES
edad = 0
ingresos = 0.0
impuesto = 0.0

# INGRESO DE DATOS
edad = int(input("Ingrese su edad: "))
ingresos = float(input("Ingrese sus ingresos mensuales: S/ "))

# PROCESO
if edad > 18 and ingresos >= 3000:
    impuesto = ingresos * 0.05
    print("El usuario SI debe tributar.")
else:
    impuesto = 0
    print("El usuario NO debe tributar.")

# SALIDA DE DATOS
print("========== RESULTADOS ==========")
print("Edad:", edad, "años")
print("Ingresos mensuales: S/", ingresos)
print("Monto a tributar: S/", round(impuesto, 2))