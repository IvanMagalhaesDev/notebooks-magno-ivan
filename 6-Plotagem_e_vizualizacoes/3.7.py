import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
n = 400

df = pd.DataFrame({
    'Type':     np.random.choice(['Bug', 'Melhoria', 'Tarefa'], size=n),
    'Priority': np.random.choice(['Baixa', 'Média', 'Alta', 'Crítica'], size=n),
    'BFT':      np.random.normal(loc=20, scale=15, size=n)
})

p95 = df['BFT'].quantile(0.95)
df_filtrado = df[(df['BFT'] > 0) & (df['BFT'] <= p95)].copy()

grafico = sns.catplot(
    data=df_filtrado,
    kind="bar",
    x='Type',
    y='BFT',
    hue='Priority',
    palette='Set2',
    height=6,
    aspect=1.5,
    errorbar=None
)

grafico.set_axis_labels("Tipo de Issue", "Média do Tempo de Resolução (BFT)")
grafico.figure.suptitle(
    f"Média de Resolução por Tipo e Prioridade\n(BFT > 0 e <= p95 [{p95:.2f}])",
    y=1.05, fontsize=14
)

plt.show()