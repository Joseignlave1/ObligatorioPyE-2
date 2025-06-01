import math
import time
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def LCG(n: int) -> list[float]:
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = int(time.time() * 1000) % m
    values = []
    for i in range(n):
        x = (a * seed + c) % m
        value = x / m
        values.append(value)
        seed = x
    return values

def graficar_uniformes(samples: list[float]):
    x_uniform = np.linspace(0, 1, 100)
    y_uniform = [1 for _ in x_uniform]

    sns.histplot(samples, bins=20, kde=True, stat="density",
                 color='skyblue', edgecolor='black', label="Muestra + KDE")
    plt.plot(x_uniform, y_uniform, label="Densidad teórica Uniforme", color='green')
    plt.title("Muestra de 100 variables uniformes en [0,1]")
    plt.xlabel("Valor")
    plt.ylabel("Densidad")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def transform_to_cauchy(uniform_samples: list[float]) -> list[float]:
    return [math.tan(math.pi * (u - 0.5)) for u in uniform_samples]

def graficar_cauchy(cauchy_samples: list[float]):
    x_vals = np.linspace(-10, 10, 1000)
    y_vals = [1 / (math.pi * (1 + x**2)) for x in x_vals]

    sns.histplot(cauchy_samples, bins=60, kde=True, stat="density",
                 color='lightcoral', edgecolor='black', label="Muestra + KDE")
    plt.plot(x_vals, y_vals, label="Densidad teórica Cauchy", color='blue')
    plt.title("Distribución Cauchy: simulación vs densidad teórica")
    plt.xlabel("Valor")
    plt.ylabel("Densidad")
    plt.legend()
    plt.grid(True)
    plt.xlim(-10, 10)
    plt.tight_layout()
    plt.show()
