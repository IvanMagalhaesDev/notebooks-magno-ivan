# %% [1]
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

df_filmes = pd.DataFrame({
    'Info_Filme': [
        "1::Toy Story (1995)::Animation|Children's|Comedy",
        "2::Jumanji (1995)::Adventure|Children's|Fantasy"
    ]
})

# %% [2] DADOS AUSENTES
print("--- Nulos por coluna ---")
display(df_olimpiadas.isnull().sum())

perc_nulos = df_olimpiadas['Age'].isnull().groupby(df_olimpiadas['Year']).mean() * 100
plt.figure(figsize=(10, 4))
perc_nulos.plot(title="% de Idades Ausentes por Ano", color='crimson')
plt.ylabel("% Nulos")
plt.xlabel("Ano")
plt.show()

display(df_olimpiadas[df_olimpiadas['Weight'].isnull()].head())

nulos_esporte = df_olimpiadas['Age'].isnull().groupby(df_olimpiadas['Sport']).mean() * 100
display(nulos_esporte.sort_values(ascending=False).head(10))

# %% [3] LIMPEZA
df_com_idade = df_olimpiadas.dropna(subset=['Age'])

mask = df_olimpiadas.drop(columns=['Medal']).notnull().all(axis=1)
df_olimp_limpo = df_olimpiadas[mask].copy()
df_olimp_limpo['Medal'] = df_olimp_limpo['Medal'].fillna('Sem Medalha')

display(df_olimp_limpo['Medal'].value_counts())

# %% [4] DUPLICATAS
print(f"Duplicatas (Olimpíadas): {df_olimp_limpo.duplicated().sum()}")
print(f"Duplicatas (Internet): {df_internet.duplicated().sum()}")

df_olimp_limpo.drop_duplicates(inplace=True)
df_internet.drop_duplicates(inplace=True)

# %% [5] OUTLIERS
plt.figure(figsize=(12, 5))
sns.boxplot(data=df_olimp_limpo, x='Year', y='Age')
plt.title("Idades por Edição das Olimpíadas")
plt.xticks(rotation=45)
plt.show()

q1 = df_internet['Velocidade_Contratada_Mbps'].quantile(0.25)
q3 = df_internet['Velocidade_Contratada_Mbps'].quantile(0.75)
lim_sup = q3 + 1.5 * (q3 - q1)

df_internet['Velocidade_Contratada_Mbps'] = df_internet['Velocidade_Contratada_Mbps'].clip(upper=lim_sup)

plt.figure(figsize=(12, 5))
sns.boxplot(data=df_internet, x='UF', y='Velocidade_Contratada_Mbps')
plt.title("Velocidade por UF (após clip)")
plt.show()

# %% [6] DISCRETIZAÇÃO
df_internet['Acessos'].plot.hist(bins=30, title="Histograma de Acessos", figsize=(8, 4))
plt.show()

df_agrupado = df_internet.groupby(['Município', 'Mês', 'Ano'])['Acessos'].sum().reset_index()
df_agrupado['Faixa_Acessos'] = pd.qcut(df_agrupado['Acessos'], q=3, labels=['Baixo', 'Médio', 'Alto'])

df_agrupado['Faixa_Acessos'].value_counts().plot.bar(color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title("Acessos por Faixa")
plt.xticks(rotation=0)
plt.show()

# %% [7] EXTRAÇÃO DE STRINGS E DUMMIES
df_filmes['Ano']    = df_filmes['Info_Filme'].str.extract(r'\((\d{4})\)')
df_filmes['Generos'] = df_filmes['Info_Filme'].str.split('::').str[2]

dummies_generos = df_filmes['Generos'].str.get_dummies(sep='|')
df_filmes_final = pd.concat([df_filmes, dummies_generos], axis=1)

display(df_filmes_final)

# %% [8] MAPEAMENTO DE REGIÕES
regioes = {
    'AC': 'Norte',       'AL': 'Nordeste',    'AP': 'Norte',       'AM': 'Norte',
    'BA': 'Nordeste',    'CE': 'Nordeste',    'DF': 'Centro-Oeste','ES': 'Sudeste',
    'GO': 'Centro-Oeste','MA': 'Nordeste',    'MT': 'Centro-Oeste','MS': 'Centro-Oeste',
    'MG': 'Sudeste',     'PA': 'Norte',       'PB': 'Nordeste',    'PR': 'Sul',
    'PE': 'Nordeste',    'PI': 'Nordeste',    'RJ': 'Sudeste',     'RN': 'Nordeste',
    'RS': 'Sul',         'RO': 'Norte',       'RR': 'Norte',       'SC': 'Sul',
    'SP': 'Sudeste',     'SE': 'Nordeste',    'TO': 'Norte'
}

df_internet['Regiao'] = df_internet['UF'].map(regioes)
display(df_internet[['UF', 'Regiao', 'Município']].head())