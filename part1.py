import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from math import exp, factorial

def analizar_cancelaciones():
    # Leer datos
    datos = pd.read_csv("cancelaciones.csv")
    cancelaciones = datos["cancelaciones"].tolist()

    # Frecuencias y probabilidades empíricas
    conteo = Counter(cancelaciones)
    valores = sorted(conteo.keys())
    frecuencias = [conteo[v] for v in valores]
    total_dias = len(cancelaciones)
    probabilidades_empiricas = [f / total_dias for f in frecuencias]
    distribucion_acumulada = np.cumsum(probabilidades_empiricas)

    tabla = pd.DataFrame({
        "Cancelaciones": valores,
        "Frecuencia absoluta": frecuencias,
        "Probabilidad empírica": probabilidades_empiricas,
        "Distribución acumulada": distribucion_acumulada
    })

    print("Tabla de frecuencias:")
    print(tabla.to_string(index=False))

    # Esperanza y varianza
    esperanza = sum([x * p for x, p in zip(valores, probabilidades_empiricas)])
    varianza = sum([(x - esperanza) ** 2 * p for x, p in zip(valores, probabilidades_empiricas)])
    print(f"Esperanza empírica: {esperanza:.2f}")
    print(f"Varianza empírica: {varianza:.2f}")

    # Mediana y RIC
    cancelaciones_ordenadas = sorted(cancelaciones)
    n = len(cancelaciones_ordenadas)
    mediana = (cancelaciones_ordenadas[n // 2] if n % 2 != 0
                else (cancelaciones_ordenadas[n // 2 - 1] + cancelaciones_ordenadas[n // 2]) / 2)
    q1 = np.percentile(cancelaciones_ordenadas, 25)
    q3 = np.percentile(cancelaciones_ordenadas, 75)
    ric = q3 - q1
    print(f"Mediana: {mediana}")
    print(f"RIC: {ric}")

    # Diagrama de caja
    plt.figure(figsize=(6, 4))
    plt.boxplot(cancelaciones, vert=False)
    plt.title("Diagrama de caja - Cancelaciones diarias")
    plt.xlabel("Cancelaciones")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("boxplot.png")
    plt.show()

    # Histograma
    plt.figure(figsize=(8, 5))
    plt.hist(cancelaciones, bins=range(min(cancelaciones), max(cancelaciones)+2),
             align='left', rwidth=0.8, color='skyblue', edgecolor='black')
    plt.title("Histograma de cancelaciones diarias")
    plt.xlabel("Número de cancelaciones")
    plt.ylabel("Frecuencia")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig("histograma.png")
    plt.show()

    # Comparación con distribución de Poisson
    lam = esperanza
    x_vals = np.arange(min(valores), max(valores) + 1)
    poisson_pmf = [((lam ** x) * exp(-lam)) / factorial(x) for x in x_vals]
    poisson_freq = [p * total_dias for p in poisson_pmf]

    plt.figure(figsize=(8, 5))
    plt.hist(cancelaciones, bins=range(min(cancelaciones), max(cancelaciones)+2),
             align='left', rwidth=0.8, color='lightgrey', edgecolor='black', label='Datos empíricos')
    plt.plot(x_vals, poisson_freq, 'o-', color='red', label='Poisson ajustada (λ = {:.2f})'.format(lam))
    plt.title("Comparación con distribución de Poisson")
    plt.xlabel("Número de cancelaciones")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("poisson_comparacion.png")
    plt.show()

    # Probabilidades
    prob_menor_5 = sum([((lam ** x) * exp(-lam)) / factorial(x) for x in range(5)])
    prob_mayor_15 = 1 - sum([((lam ** x) * exp(-lam)) / factorial(x) for x in range(16)])
    print(f"P(X < 5) ≈ {prob_menor_5:.4f}")
    print(f"P(X > 15) ≈ {prob_mayor_15:.4f}")
