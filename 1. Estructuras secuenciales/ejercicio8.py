# ENTRADA: Solicitar las medidas de los tres lados
lado1 = float(input("Ingrese la medida del lado 1: "))
lado2 = float(input("Ingrese la medida del lado 2: "))
lado3 = float(input("Ingrese la medida del lado 3: "))
# PROCESO: Calcular el semiperimetro
semiperimetro = (lado1 + lado2 + lado3) / 2
# Calcular el area del terreno
area = (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5
# SALIDA: Mostrar el resultado
print("El semiperimetro es:", semiperimetro)
print("El area del terreno es:", area, "m2")