import pandas as pd
from IPython.display import display

tab_esq = pd.DataFrame({'lk': ['A', 'B', 'C', 'A'], 'v': [1, 2, 3, 4]})
tab_dir = pd.DataFrame({'rk': ['A', 'B', 'D'], 'v': [10, 20, 30]})

print("Tabela Esquerda:")
display(tab_esq)
print("\nTabela Direita:")
display(tab_dir)

print("\n--- Merge outer com sufixos e indicator ---")
resultado = pd.merge(
    tab_esq, tab_dir,
    left_on="lk", right_on="rk",
    how="outer",
    suffixes=("_esq", "_dir"),
    indicator=True
)
display(resultado)
display(resultado['_merge'].value_counts())

print("\n--- validate='m:1' ---")
try:
    pd.merge(tab_esq, tab_dir, left_on="lk", right_on="rk", validate="m:1")
    print("OK: validate='m:1' passou.")
except Exception as erro:
    print(f"Erro: {erro}")

dir_duplicada = pd.DataFrame({'rk': ['A', 'A', 'B'], 'v': [10, 15, 20]})

try:
    pd.merge(tab_esq, dir_duplicada, left_on="lk", right_on="rk", validate="m:1")
except Exception as erro:
    print(f"MergeError capturado: {erro}")

try:
    pd.merge(tab_esq, dir_duplicada, left_on="lk", right_on="rk", validate="m:m")
    print("OK: validate='m:m' passou.")
except Exception as erro:
    print(f"Erro: {erro}")