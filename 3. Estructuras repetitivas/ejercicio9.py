
# IDENTIFICACIÓN DE VARIABLES

numeros = []
i = 0
producto = 1

# INGRESO DE DATOS

# No se requiere ingreso de datos,
# porque la secuencia está establecida.

# PROCESO

# GENERAR LOS NUMEROS PARES DE 100 HASTA 2

numeros = list(range(100, 0, -2))

# AGREGAR EL NUMERO 1 AL FINAL

numeros.append(1)

# CALCULAR EL PRODUCTO

for i in range(0, len(numeros)):

    producto = producto * numeros[i]

# SALIDA DE DATOS

print("======= SECUENCIA DE NUMEROS =======")

print(" x ".join(map(str, numeros)))

print("\n======= RESULTADO =======")
print("Cantidad de elementos:", len(numeros))
print("Producto total:", producto)