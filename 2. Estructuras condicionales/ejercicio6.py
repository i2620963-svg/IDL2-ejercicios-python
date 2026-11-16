# IDENTIFICACIÓN DE VARIABLES
lado1 = 0.0
lado2 = 0.0
lado3 = 0.0
perimetro = 0.0
semiperimetro = 0.0
area = 0.0

# INGRESO DE DATOS
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

# PROCESO
# Verificar si los lados forman un triángulo
if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Los lados deben ser mayores que cero.")

elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("Los lados ingresados no forman un triángulo.")
    
# Identificar si es equilátero
elif lado1 == lado2 and lado2 == lado3:
    perimetro = lado1 + lado2 + lado3

    print("El triángulo es EQUILÁTERO.")
    print("Perímetro:", perimetro)

# Identificar si es isósceles
elif lado1 == lado2:
    print("El triángulo es ISÓSCELES.")
    print("Los lados iguales son:", lado1, "y", lado2)

elif lado1 == lado3:
    print("El triángulo es ISÓSCELES.")
    print("Los lados iguales son:", lado1, "y", lado3)

elif lado2 == lado3:
    print("El triángulo es ISÓSCELES.")
    print("Los lados iguales son:", lado2, "y", lado3)

# Identificar si es escaleno
else:
    semiperimetro = (lado1 + lado2 + lado3) / 2

    area = (semiperimetro * (semiperimetro - lado1) *
            (semiperimetro - lado2) *
            (semiperimetro - lado3)) ** 0.5

    print("El triángulo es ESCALENO.")
    print("Área del triángulo:", round(area, 2))