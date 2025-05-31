import math
import time
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Parte 1 - Simulación de variables uniformes en [0,1]
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

# Parte 2 - Generar muestra uniforme y graficar
samples = LCG(100)

sns.histplot(samples, bins=20, kde=True, stat="density", color='skyblue', edgecolor='black')
plt.title("Muestra de 100 variables uniformes en [0,1]")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.grid(True)
plt.tight_layout()
plt.show()


# Parte 3 y 4 Transformación por función inversa a distribucción de Cauchy estándar
def transform_to_cauchy(uniform_samples: list[float]) -> list[float]:
    cauchy_samples = []
    for u in uniform_samples:
        x = math.tan(math.pi * (u - 0.5))
        cauchy_samples.append(x)
    return cauchy_samples

# Parte 5 - Muestra de tamaño 100 de variables aleatorias independientes, con distribución de Cauchy, superponiendo en el gráfico la densidad teórica de la cauchy estandar.
def densidad_cauchy(x):
    return 1 / (math.pi * (1 + x**2))

x_vals = np.linspace(-10, 10, 1000)
y_vals = [densidad_cauchy(x) for x in x_vals]


cauchy_samples = transform_to_cauchy(samples)

sns.histplot(cauchy_samples, bins=60, kde=True, stat="density", color='lightcoral', edgecolor='black', label="Muestra + KDE")
plt.plot(x_vals, y_vals, label="Densidad teórica Cauchy", color='blue')
plt.title("Distribución Cauchy: simulación vs densidad teórica")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.legend()
plt.grid(True)
plt.xlim(-10, 10)
plt.tight_layout()
plt.show()
