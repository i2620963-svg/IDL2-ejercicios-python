# ENTRADA: Solicitar los datos
sueldo_base = float(input("Ingrese el sueldo base: "))
venta1 = float(input("Ingrese el monto de la venta 1: "))
venta2 = float(input("Ingrese el monto de la venta 2: "))
venta3 = float(input("Ingrese el monto de la venta 3: "))
# PROCESO: Calcular las ventas y comisiones
comision = 0.25
total_ventas = venta1 + venta2 + venta3
total_comisiones = total_ventas * comision
total_mes = sueldo_base + total_comisiones
# SALIDA: Mostrar los resultados
print("Total de ventas: S/", total_ventas)
print("Total de comisiones: S/", total_comisiones)
print("Total a recibir en el mes: S/", total_mes)