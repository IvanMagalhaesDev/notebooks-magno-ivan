import pandas as pd
import numpy as np
from IPython.display import display

datas = pd.date_range("2023-01-01", periods=3)
df_largo = pd.DataFrame(
    {"item1": [10, 20, 30], "item2": [40, 50, 60]},
    index=datas
)
df_largo.index.name = "date"
df_largo.columns.name = "item"

print("1. Formato Largo (Wide):")
display(df_largo)

print("\n2. Formato Longo com stack:")
df_longo = df_largo.stack().reset_index().rename(columns={0: "value"})
display(df_longo)

print("\n3. De volta ao Largo com pivot:")
display(df_longo.pivot(index="date", columns="item", values="value"))

print("\n4. Pivot com múltiplas colunas de valor:")
df_longo["value2"] = np.random.randint(100, 200, size=len(df_longo))
display(df_longo.pivot(index="date", columns="item"))

print("\n5. pd.melt e reversão com pivot:")
df_base = pd.DataFrame({"key": ["k1", "k2"], "A": [1, 2], "B": [3, 4], "C": [5, 6]})

df_derretido = pd.melt(df_base, id_vars=["key"], value_vars=["A", "B", "C"],
                       var_name="variavel", value_name="valor")
display(df_derretido)

df_reconstruido = df_derretido.pivot(index="key", columns="variavel", values="valor").reset_index()
df_reconstruido.columns.name = None
display(df_reconstruido)