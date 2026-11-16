# IDENTIFICACIÓN DE VARIABLES
num1 = 0.0
num2 = 0.0
num3 = 0.0
mayor = 0.0
menor = 0.0

# INGRESO DE DATOS
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# PROCESO
# Determinar el número mayor
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Determinar el número menor
if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

# SALIDA DE DATOS
print("========== RESULTADOS ==========")
print("El número mayor es:", mayor)
print("El número menor es:", menor)