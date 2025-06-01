from part1 import analizar_cancelaciones
from part2 import LCG, graficar_uniformes, transform_to_cauchy, graficar_cauchy

def main():
    uniform_samples = []
    while True:
        print("\n--- MENÚ INTERACTIVO ---")
        print("1. Problema 1 - cancelación de cuentas en una aplicación Web")
        print("2. Problema 2 - Generar y graficar variables uniformes")
        print("3. Problema 2 - Transformar muestra a Cauchy y graficar")
        print("4. Salir")

        opcion = input("Elegí una opción (1-4): ")

        if opcion == "1":
            analizar_cancelaciones()

        elif opcion == "2":
            uniform_samples = LCG(100)
            graficar_uniformes(uniform_samples)

        elif opcion == "3":
            if not uniform_samples:
                print("⚠️ Primero generá las muestras uniformes (opción 1).")
            else:
                cauchy_samples = transform_to_cauchy(uniform_samples)
                graficar_cauchy(cauchy_samples)
        elif opcion == "4":
            print("Programa finalizado correctamente.")
            break

        else:
            print("❌ Opción inválida. Intentá de nuevo.")

if __name__ == "__main__":
    main()
