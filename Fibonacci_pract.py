
import time

def fibonacci(n):
    a, b = 0, 1
    serie = []

    for i in range(n):
        serie.append(a)
        a, b = b, a + b

    return serie


def main():
    print("=" * 40)
    print("       SERIE DE FIBONACCI")
    print("=" * 40)

    while True:
        try:
            cantidad = int(
                input("¿Cuántos números deseas generar?: ")
            )

            if cantidad <= 0:
                print("Ingresa un número mayor que cero.")
                continue

            break

        except ValueError:
            print("Error: debes ingresar un número entero.")

    inicio = time.perf_counter()
    resultado = fibonacci(cantidad)
    fin = time.perf_counter()

    print("\nSerie de Fibonacci:")
    print(*resultado, sep=", ")

    print(f"\nCantidad de números: {cantidad}")
    print(f"Tiempo de ejecución: {(fin - inicio):.8f} segundos")


if __name__ == "__main__":
    main()
