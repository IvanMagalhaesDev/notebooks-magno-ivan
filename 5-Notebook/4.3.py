import pandas as pd
import numpy as np
from IPython.display import display

np.random.seed(42)

idx_linhas = pd.MultiIndex.from_product([['A', 'B'], [1, 2]], names=['k', 'j'])
idx_colunas = pd.MultiIndex.from_product([['X', 'Y'], ['val1', 'val2']], names=['axis', 'var'])

df = pd.DataFrame(
    np.random.randint(1, 10, size=(4, 4)),
    index=idx_linhas,
    columns=idx_colunas
)

print("DataFrame Original:")
display(df)

print("\n--- Soma agrupada pelo nível 'k' ---")
display(df.groupby(level='k').sum())

print("\n--- Média agrupada pelo nível 'axis' nas colunas ---")
display(df.T.groupby(level='axis').agg('mean').T)