import pandas as pd
from IPython.display import display

df_esq = pd.DataFrame({"v": [1, 2, 3]}, index=list("abc"))
df_dir = pd.DataFrame({"w": [10, 20]}, index=list("ab"))

idx_multi = pd.MultiIndex.from_arrays([list("AABBB"), [1, 1, 2, 2, 3]], names=["g", "k"])
df_multi  = pd.DataFrame({"z": [5, 6, 7, 8, 9]}, index=idx_multi)
df_colunas = pd.DataFrame({"g": list("AABAB"), "k": [1, 2, 1, 3, 2], "t": range(5)})

print("Merge por índice (outer):")
display(pd.merge(df_esq, df_dir, left_index=True, right_index=True, how="outer"))

print("Join por índice (outer):")
display(df_esq.join(df_dir, how="outer"))

print("Merge INNER — colunas vs. MultiIndex:")
display(pd.merge(df_colunas, df_multi, left_on=["g", "k"], right_index=True))

print("Merge OUTER — colunas vs. MultiIndex:")
display(pd.merge(df_colunas, df_multi, left_on=["g", "k"], right_index=True, how="outer"))