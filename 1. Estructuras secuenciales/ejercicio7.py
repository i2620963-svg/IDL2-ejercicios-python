# ENTRADA: Solicitar el tiempo de estacionamiento
horas = int(input("Ingrese las horas de estacionamiento: "))
minutos = int(input("Ingrese los minutos restantes: "))
# PROCESO: Calcular el importe a pagar
tarifa_hora = 5.00
horas_cobro = horas + (minutos + 59) // 60
total = horas_cobro * tarifa_hora
# SALIDA: Mostrar el resultado
print("Horas cobradas:", horas_cobro)
print("Total a pagar: S/", total)