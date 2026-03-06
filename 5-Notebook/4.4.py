import pandas as pd

df = pd.DataFrame({
    'a': [1, 2, 3, 4],
    'b': ['X', 'X', 'Y', 'Y'],
    'c': ['Alfa', 'Beta', 'Alfa', 'Beta'],
    'd': [100, 200, 300, 400]
})

print("DataFrame de partida:")
display(df)

print("\n--- set_index com drop=False ---")
df_indexado = df.set_index(['b', 'c'], drop=False)
display(df_indexado)

print("\n--- reset_index com drop=True ---")
df_resetado = df_indexado.reset_index(drop=True)
display(df_resetado)