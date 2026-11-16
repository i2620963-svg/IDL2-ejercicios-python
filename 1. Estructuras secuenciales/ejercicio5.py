# ENTRADA: Solicitar los datos
capital = float(input("Ingrese el capital a invertir: "))
# PROCESO: Calcular el interés y el monto total
tasa = 0.02
meses = 12
interes = capital * tasa * meses
total = capital + interes
# SALIDA: Mostrar los resultados
print("El interés ganado en un año es: S/", interes)
print("El monto total acumulado es: S/", total)