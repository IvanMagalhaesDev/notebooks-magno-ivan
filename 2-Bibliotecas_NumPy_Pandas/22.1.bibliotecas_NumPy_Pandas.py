# %% [1]
import numpy as np
import pandas as pd

# %% [2] EXERCÍCIO 1.13.1
print("--- Exercício 1.13.1 ---")
vetor = np.arange(1, 11)
print(f"Array: {vetor}")
print(f"Dtype: {vetor.dtype} | Shape: {vetor.shape} | Ndim: {vetor.ndim}\n")

# %% [3] EXERCÍCIO 1.13.2
print("--- Exercício 1.13.2 ---")
matriz = np.arange(12).reshape(3, 4)
print("Matriz 3x4:\n", matriz)
print("Soma por linha:", matriz.sum(axis=1))
print("Soma por coluna:", matriz.sum(axis=0), "\n")

# %% [4] EXERCÍCIO 1.13.3
print("--- Exercício 1.13.3 ---")
vet_a = np.array([10, 20, 30, 40, 50])
vet_b = np.array([2, 4, 5, 8, 10])
print("Adição:", vet_a + vet_b)
print("Subtração:", vet_a - vet_b)
print("Multiplicação:", vet_a * vet_b)
print("Divisão:", vet_a / vet_b, "\n")

# %% [5] EXERCÍCIO 1.13.4
print("--- Exercício 1.13.4 ---")
mat4x4 = np.arange(1, 17).reshape(4, 4)
print("Matriz original:\n", mat4x4)
print("\nLinha 2:", mat4x4[1, :])
print("Coluna 3:", mat4x4[:, 2])
print("Submatriz (2 últimas linhas e colunas):\n", mat4x4[2:, 2:], "\n")

# %% [6] EXERCÍCIO 1.13.5
print("--- Exercício 1.13.5 ---")
periodo_inicial = np.array([100, 150, 200, 250])
periodo_final   = np.array([120, 165, 240, 260])
ica = ((periodo_final - periodo_inicial) / periodo_inicial) * 100
print("ICA:", ica)
print("Média:", ica.mean(), "\n")

# %% [7] EXERCÍCIO 2.5.1
print("--- Exercício 2.5.1 ---")
serie = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("Valor em 'c':", serie['c'])
print("Dtype:", serie.dtype)
print("Índices:", serie.index, "\n")

# %% [8] EXERCÍCIOS 2.5.2 e 2.5.3
print("--- Exercícios 2.5.2 e 2.5.3 ---")
df_pessoas = pd.DataFrame({
    'nome':   ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'idade':  [23, 35, 19, 42],
    'cidade': ['Fortaleza', 'São Paulo', 'Recife', 'Manaus']
})
display(df_pessoas.head(2))
print(df_pessoas['cidade'])
print("Média de idade:", df_pessoas['idade'].mean())
display(df_pessoas.sort_values(by='idade', ascending=False))

# %% [9] EXERCÍCIO 2.5.5
print("--- Exercício 2.5.5 ---")
serie_rep = pd.Series(['a', 'b', 'a', 'c', 'b', 'b', 'd'])
print("Únicos:", serie_rep.unique())
print(serie_rep.value_counts(), "\n")

# %% [10] CARREGAMENTO
caminho_yahoo = "./files/yahoo_price.pkl"
caminho_olimp = "./files/atletas_eventos_olimpiadas.csv"

try:
    df_yahoo = pd.read_pickle(caminho_yahoo)
    df_olimp = pd.read_csv(caminho_olimp)
    arquivos_ok = True
    print("Datasets carregados com sucesso!")
except FileNotFoundError:
    arquivos_ok = False
    print("Arquivos não encontrados.")

# %% [11] EXERCÍCIOS 2.5.6, 2.5.7 e 2.5.8
if arquivos_ok:
    print("--- Exercício 2.5.6 ---")
    display(df_yahoo.head(5))
    print(df_yahoo.filter(regex='^A', axis=1).mean())

    print("\n--- Exercício 2.5.7 ---")
    n_original = len(df_yahoo)
    df_yahoo_sem_nan = df_yahoo.dropna()
    print(f"Antes: {n_original} | Depois: {len(df_yahoo_sem_nan)}")

    print("\n--- Exercício 2.5.8 ---")
    desvios = df_yahoo.ffill().std()
    print(desvios.sort_values(ascending=False).head(3))

# %% [12] EXERCÍCIOS 3.3.1 a 3.3.3
if arquivos_ok:
    print("--- Exercício 3.3.1 ---")
    display(df_olimp.groupby('Games')['Age'].mean().head())

    print("\n--- Exercício 3.3.2 ---")
    media_altura = df_olimp.groupby('Team')['Height'].mean()
    print(f"{media_altura.idxmax()} ({media_altura.max():.2f} cm)")

    print("\n--- Exercício 3.3.3 ---")
    display(df_olimp.dropna(subset=['Medal']).groupby(['Sex', 'Medal']).size())

# %% [13] EXERCÍCIOS 3.3.4 a 3.3.6
if arquivos_ok:
    print("--- Exercício 3.3.4 ---")
    com_medalha = df_olimp.dropna(subset=['Medal'])
    idx_vet = com_medalha.groupby('Sport')['Age'].idxmax()
    display(com_medalha.loc[idx_vet, ['Sport', 'Name', 'Age']].head())

    print("\n--- Exercício 3.3.5 ---")
    variab = df_olimp.groupby("Games")["Age"].std()
    print(f"{variab.idxmax()} (DP: {variab.max():.2f})")

    print("\n--- Exercício 3.3.6 ---")
    nocs_ouro = com_medalha[com_medalha['Medal'] == 'Gold']['NOC'].unique()
    sem_ouro  = com_medalha[~com_medalha['NOC'].isin(nocs_ouro)]
    display(sem_ouro['NOC'].value_counts().head(5))