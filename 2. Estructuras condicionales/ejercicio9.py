# IDENTIFICACIÓN DE VARIABLES
cantidad = 0
precio = 0.0
subtotal = 0.0
porcentaje = 0.0
descuento = 0.0
total = 0.0

# INGRESO DE DATOS
cantidad = int(input("Ingrese la cantidad de camisetas: "))
precio = float(input("Ingrese el precio unitario de cada camiseta: S/ "))

# PROCESO

# Calcular el importe total sin descuento
subtotal = cantidad * precio

# Determinar el porcentaje de descuento
if cantidad >= 1 and cantidad <= 4:
    porcentaje = 0.125

elif cantidad >= 5 and cantidad <= 8:
    porcentaje = 0.20

elif cantidad > 8:
    porcentaje = 0.315

else:
    porcentaje = 0

# Calcular el descuento y el total a pagar
descuento = subtotal * porcentaje
total = subtotal - descuento

# SALIDA DE DATOS
print("========== DETALLE DE COMPRA ==========")
print("Cantidad de camisetas:", cantidad)
print("Compra sin descuento: S/", round(subtotal, 2))
print("Porcentaje de descuento:", porcentaje * 100, "%")
print("Monto del descuento: S/", round(descuento, 2))
print("Compra final con descuento: S/", round(total, 2))