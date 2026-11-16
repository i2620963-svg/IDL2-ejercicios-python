# ENTRADA: Solicitar las inversiones
inversion1 = float(input("Ingrese la inversión de la persona 1: "))
inversion2 = float(input("Ingrese la inversión de la persona 2: "))
inversion3 = float(input("Ingrese la inversión de la persona 3: "))

# PROCESO: Calcular el total invertido
total = inversion1 + inversion2 + inversion3

# Calcular el porcentaje de cada persona
porcentaje1 = (inversion1 / total) * 100
porcentaje2 = (inversion2 / total) * 100
porcentaje3 = (inversion3 / total) * 100

# SALIDA: Mostrar los resultados
print("Total invertido: S/", total)
print("Porcentaje de la persona 1:", porcentaje1, "%")
print("Porcentaje de la persona 2:", porcentaje2, "%")
print("Porcentaje de la persona 3:", porcentaje3, "%")