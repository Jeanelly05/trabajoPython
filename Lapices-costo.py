import pandas as pd
import matplotlib.pyplot as plt

file_path = "./Data/Pen Sales Data.xlsx"
df_pen_sales = pd.read_excel(file_path, sheet_name="Pen Sales")
#2Analisis de costos de envio

df_avg_pen_costs = df_pen_sales.groupby("Item")["Shipping Cost"].mean().sort_values()
print(df_avg_pen_costs)

plt.figure(figsize = (10,5))
df_avg_pen_costs.plot(kind="barh", color="purple")
plt.title("Costo de envio promedio por producto")
plt.xlabel("Costo medio de envio")
plt.ylabel("Tipo de producto")
plt.show()
