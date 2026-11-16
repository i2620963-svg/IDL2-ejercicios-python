# ENTRADA: Solicitar los datos de la compra
monto_base = float(input("Ingrese el monto base de la compra: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))
dinero_pago = float(input("Ingrese el dinero entregado por el cliente: "))
# PROCESO: Calcular el descuento
descuento = (monto_base * porcentaje) / 100
# Calcular el total a pagar
total_pagar = monto_base - descuento
# Calcular el cambio
cambio = dinero_pago - total_pagar
# SALIDA: Mostrar los resultados
print("Monto del descuento: S/", descuento)
print("Total a pagar: S/", total_pagar)
print("Cambio a recibir: S/", cambio)