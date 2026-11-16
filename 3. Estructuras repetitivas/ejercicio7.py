# IDENTIFICACIÓN DE VARIABLES

num1 = 0
num2 = 0
i = 0

factorial1 = 1
factorial2 = 1

desarrollo1 = ""
desarrollo2 = ""

limite = 0

# INGRESO DE DATOS

while True:

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if num1 >= 0 and num2 >= 0:
        break
    else:
        print("Error: Ingrese números positivos o cero.")

# PROCESO

# CALCULAR EL FACTORIAL DEL PRIMER NUMERO

for i in range(1, num1 + 1):

    factorial1 = factorial1 * i

    if i == 1:
        desarrollo1 = str(i)
    else:
        desarrollo1 = desarrollo1 + " x " + str(i)

# CALCULAR EL FACTORIAL DEL SEGUNDO NUMERO

for i in range(1, num2 + 1):

    factorial2 = factorial2 * i

    if i == 1:
        desarrollo2 = str(i)
    else:
        desarrollo2 = desarrollo2 + " x " + str(i)

# CONTROLAR EL FACTORIAL DE CERO

if num1 == 0:
    desarrollo1 = "1"

if num2 == 0:
    desarrollo2 = "1"

# DETERMINAR HASTA QUE FACTOR COINCIDEN

if num1 < num2:
    limite = num1
else:
    limite = num2

# SALIDA DE DATOS

print("\n========== RESULTADOS ==========")

print("\nFACTORIAL DEL PRIMER NUMERO")
print(num1, "! =", desarrollo1, "=", factorial1)

print("\nFACTORIAL DEL SEGUNDO NUMERO")
print(num2, "! =", desarrollo2, "=", factorial2)

print("\n========== COMPARACION ==========")

if limite > 0:
    print("Son iguales hasta el factor:", limite)
else:
    print("No existen factores comunes en la secuencia.")