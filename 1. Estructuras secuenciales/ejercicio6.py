# ENTRADA: Solicitar la edad de la persona
edad = int(input("Ingrese su edad en años: "))
# PROCESO: Calcular el tiempo vivido
meses = edad * 12
semanas = edad * 52
dias = edad * 365
horas = dias * 24
# SALIDA: Mostrar los resultados
print("Meses vividos:", meses)
print("Semanas vividas:", semanas)
print("Días vividos:", dias)
print("Horas vividas:", horas)