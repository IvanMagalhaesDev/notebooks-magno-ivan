import pandas as pd
import numpy as np
from IPython.display import display

pares = [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]
idx = pd.MultiIndex.from_tuples(pares, names=['outer', 'inner'])
serie = pd.Series(np.random.randint(10, 100, size=6), index=idx)

print("Series com MultiIndex:")
display(serie)

print("\n--- Rótulo externo 'b' ---")
display(serie.loc['b'])

print("\n--- Nível interno igual a 2 ---")
display(serie.loc[:, 2])

print("\n--- unstack() ---")
serie_unstacked = serie.unstack()
display(serie_unstacked)

print("\n--- stack() ---")
display(serie_unstacked.stack())

print("\n--- unstack(level='outer') ---")
display(serie.unstack(level="outer"))