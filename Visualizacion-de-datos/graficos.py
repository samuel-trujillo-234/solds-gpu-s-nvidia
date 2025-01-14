# Guardar los gráficos en lugar de mostrarlos

# Crear carpeta "imagenes" si no existe
import os

output_dir = "imagenes"
os.makedirs(output_dir, exist_ok=True)

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
output_path = os.path.join(output_dir, "evolucion_ventas.png")
plt.savefig(output_path, dpi=300)
plt.close()

# Gráfico de barras comparativo (series normales vs Ti)
plt.figure(figsize=(10, 6))
sns.barplot(data=df_barras, x="Tipo", y="Ventas", ci=None, palette="viridis", estimator=sum)
plt.title("Comparación de Ventas: Normales vs Ti", fontsize=14)
plt.xlabel("Tipo de Serie", fontsize=12)
plt.ylabel("Ventas Totales", fontsize=12)
output_path = os.path.join(output_dir, "comparacion_normales_vs_ti.png")
plt.savefig(output_path, dpi=300)
plt.close()

output_dir
