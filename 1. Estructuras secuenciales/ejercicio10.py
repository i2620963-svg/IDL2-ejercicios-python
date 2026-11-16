# ENTRADA: Solicitar la cantidad a retirar
retiro = int(input("Ingrese la cantidad a retirar: "))
# PROCESO: Calcular los billetes y monedas
b200 = retiro // 200
restante = retiro % 200
b100 = restante // 100
restante = restante % 100
b50 = restante // 50
restante = restante % 50
b20 = restante // 20
restante = restante % 20
b10 = restante // 10
restante = restante % 10
b5 = restante // 5
restante = restante % 5
m1 = restante // 1
total_piezas = b200 + b100 + b50 + b20 + b10 + b5 + m1
# SALIDA: Mostrar los resultados
print("Billetes de S/ 200:", b200)
print("Billetes de S/ 100:", b100)
print("Billetes de S/ 50:", b50)
print("Billetes de S/ 20:", b20)
print("Billetes de S/ 10:", b10)
print("Billetes de S/ 5:", b5)
print("Monedas de S/ 1:", m1)
print("Total de billetes y monedas:", total_piezas)