import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Crear un conjunto de datos ficticio
np.random.seed(42)  # Para reproducibilidad

# Años, regiones y series
years = list(range(2018, 2024))
regions = ["América del Norte", "Europa", "Asia-Pacífico", "América Latina"]
series = ["1000", "1000 Ti", "2000", "2000 Ti", "3000", "3000 Ti", "4000", "4000 Ti"]

# Generar datos aleatorios para ventas
data = []
for year in years:
    for region in regions:
        for serie in series:
            sales = np.random.randint(500, 5000)  # Ventas aleatorias
            data.append({"Año": year, "Región": region, "Serie": serie, "Ventas": sales})

# Crear DataFrame
df = pd.DataFrame(data)

# Agregar crecimiento porcentual de un año al siguiente (ficticio para la demo)
df["Crecimiento (%)"] = df.groupby(["Región", "Serie"])["Ventas"].pct_change().fillna(0) * 100

# Resumen de ventas por año
ventas_anuales = df.groupby(["Año", "Serie"])["Ventas"].sum().reset_index()

# Resumen de ventas por región
ventas_regionales = df.groupby(["Región"])["Ventas"].sum().reset_index()

# --- Gráficos ---

# Gráfico de series temporales (evolución de ventas por año)
plt.figure(figsize=(12, 6))
for serie in ["1000", "2000", "3000", "4000"]:
    subset = ventas_anuales[ventas_anuales["Serie"] == serie]
    plt.plot(subset["Año"], subset["Ventas"], marker="o", label=f"Serie {serie}")

plt.title("Evolución de Ventas por Serie Normal (2018-2023)", fontsize=14)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Ventas (en miles)", fontsize=12)
plt.legend(title="Serie", fontsize=10)
plt.grid(True)
plt.show()

# Gráfico de barras comparativo (series normales vs Ti)
df_barras = df.groupby(["Serie"]).sum().reset_index()
df_barras["Tipo"] = df_barras["Serie"].apply(lambda x: "Ti" if "Ti" in x else "Normal")

plt.figure(figsize=(10, 6))
sns.barplot(data=df_barras, x="Tipo", y="Ventas", ci=None, palette="viridis", estimator=sum)
plt.title("Comparación de Ventas: Normales vs Ti", fontsize=14)
plt.xlabel("Tipo de Serie", fontsize=12)
plt.ylabel("Ventas Totales", fontsize=12)
plt.show()
