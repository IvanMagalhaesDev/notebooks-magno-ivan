import pandas as pd
import numpy as np
from IPython.display import display

np.random.seed(42)
pares = [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]
idx = pd.MultiIndex.from_tuples(pares, names=['outer', 'inner'])
serie = pd.Series(np.random.randint(10, 100, size=6), index=idx)

print("Series Original:")
display(serie)

print("\n--- swaplevel ---")
serie_trocada = serie.swaplevel("outer", "inner")
display(serie_trocada)

print("\n--- sort_index pelo nível interno ---")
serie_ord = serie.sort_index(level="inner")
display(serie_ord)

print("\n--- swaplevel + sort_index encadeados ---")
serie_final = serie.swaplevel("outer", "inner").sort_index(level=0)
display(serie_final)