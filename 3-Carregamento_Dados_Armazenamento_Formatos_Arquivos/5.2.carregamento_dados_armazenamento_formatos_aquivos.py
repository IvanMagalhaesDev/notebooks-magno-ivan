# %% [1]
import pandas as pd
import requests

# %% [2] EXERCÍCIO 5.1
print("--- Exercício 5.1 ---")
df_ex1 = pd.read_csv("examples/ex1.csv")
display(df_ex1.head())

# %% [3] EXERCÍCIO 5.2
print("--- Exercício 5.2 ---")
cols = ["a", "b", "c", "d", "message"]
df_renomeado = pd.read_csv("examples/ex1.csv", header=None, names=cols, index_col="message")
display(df_renomeado.head())

# %% [4] EXERCÍCIO 5.3
print("--- Exercício 5.3 ---")
display(pd.read_csv("examples/ex3.txt", sep=r"\s+").head())

# %% [5] EXERCÍCIO 5.4
print("--- Exercício 5.4 ---")
df_nulos = pd.read_csv("examples/ex5.csv", keep_default_na=False, na_values=["NULL", "NA"])
display(df_nulos.isna())

# %% [6] EXERCÍCIO 5.5
print("--- Exercício 5.5 ---")
pedacos = pd.read_csv("examples/ex6.csv", chunksize=500)
contagem = pd.Series([], dtype='int64')

for bloco in pedacos:
    contagem = contagem.add(bloco["key"].value_counts(), fill_value=0)

display(contagem.sort_values(ascending=False).head(10))

# %% [7] EXERCÍCIO 5.6
print("--- Exercício 5.6 ---")
df_json = pd.read_json("examples/example.json")
df_json.drop(columns=["b"], inplace=True)
df_json.to_json("examples/example_modified.json")
print("Arquivo salvo em: examples/example_modified.json")

# %% [8] EXERCÍCIO 5.7
print("--- Exercício 5.7 ---")
resposta = requests.get("https://api.github.com/repos/pandas-dev/pandas/issues")
resposta.raise_for_status()

df_issues = pd.DataFrame(resposta.json(), columns=["number", "title", "state", "labels"])
df_issues.to_parquet("examples/issues.parquet")

print("Issues salvas em: examples/issues.parquet")
display(df_issues.head())