# IDENTIFICACIÓN DE VARIABLES
cantidad = 0
promedio = 0.0
costo = 100.0
subtotal = 0.0
descuento = 0.0
total = 0.0
mitad = 0

# INGRESO DE DATOS
cantidad = int(input("Ingrese la cantidad de materias: "))
promedio = float(input("Ingrese el promedio del último periodo: "))

# PROCESO
subtotal = cantidad * costo

if promedio >= 18:
    mitad = cantidad // 2
    descuento = (mitad * costo) * 0.50
else:
    descuento = 0

total = subtotal - descuento

# SALIDA DE DATOS

print("========== COLEGIATURA ==========")
print("Cantidad de materias:", cantidad)
print("Promedio obtenido:", promedio)
print("Costo total: S/", subtotal)
print("Descuento aplicado: S/", descuento)
print("Total a pagar: S/", total)