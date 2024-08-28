def fibonacci(n):
    # Crear una lista para almacenar la serie de Fibonacci
    serie = []
    # Los dos primeros elementos de la serie son 0 y 1
    a=0
    b=1
    while len(serie) < n:
        serie.append(a)
        a, b = b, a + b  # Actualizar los valores de a y b
    return serie
# Solicitar al usuario la cantidad de elementos
n = int(input("Introduce el número de elementos de la serie de Fibonacci: "))

# Generar la serie de Fibonacci
resultado = fibonacci(n)
# Imprimir la serie de Fibonacci
print("La serie de Fibonacci con", n, "elementos es:", resultado)
