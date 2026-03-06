import pandas as pd
from IPython.display import display

esquerda = pd.DataFrame({'key': ['a', 'b', 'b', 'c'], 'valor_esq': [1, 2, 3, 4]})
direita  = pd.DataFrame({'key': ['a', 'b', 'd'], 'valor_dir': [10, 20, 30]})

print("DataFrame Esquerda:")
display(esquerda)
print("\nDataFrame Direita:")
display(direita)

print("\n--- INNER ---")
resultado_inner = pd.merge(esquerda, direita, on="key", how="inner")
display(resultado_inner)
display(resultado_inner['key'].value_counts())

print("\n--- LEFT ---")
display(pd.merge(esquerda, direita, on="key", how="left"))

print("\n--- OUTER ---")
display(pd.merge(esquerda, direita, on="key", how="outer"))