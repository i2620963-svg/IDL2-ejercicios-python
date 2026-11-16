# IDENTIFICACIÓN DE VARIABLES
cantidad = 0
precio = 0.0
total = 0.0
# INGRESO DE DATOS
cantidad = int(input("Ingrese la cantidad de llantas: "))
# PROCESO
if cantidad < 5:
    precio = 150
else:
    precio = 120
total = cantidad * precio
# SALIDA DE DATOS
print("========== LLANTERA ==========")
print("Cantidad de llantas:", cantidad)
print("Precio por llanta: S/", precio)
print("Total a pagar: S/", total)