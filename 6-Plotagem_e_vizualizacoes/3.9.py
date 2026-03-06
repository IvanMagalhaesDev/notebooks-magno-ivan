import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

np.random.seed(42)
datas = pd.date_range(start='2023-01-01', end='2023-12-31', periods=800)
prioridades = np.random.choice(['Baixa', 'Média', 'Alta', 'Crítica'], size=800, p=[0.4, 0.35, 0.2, 0.05])

df = pd.DataFrame({'CreationDate': datas, 'Priority': prioridades})
df['CreationDate'] = pd.to_datetime(df['CreationDate'])
df_idx = df.set_index('CreationDate')

top_3 = df['Priority'].value_counts().head(3).index.tolist()

fig, ax = plt.subplots(figsize=(12, 6))

estilos = ['-', '--', '-.']
cores   = ['#1f77b4', '#ff7f0e', '#2ca02c']

for i, prioridade in enumerate(top_3):
    contagem = df_idx[df_idx['Priority'] == prioridade].resample('ME').size()
    ax.plot(
        contagem.index, contagem.values,
        label=f"{prioridade} (Top {i+1})",
        linestyle=estilos[i],
        color=cores[i],
        marker='o',
        linewidth=2
    )

ax.legend(loc="best", title="Prioridades", fontsize=10)
ax.set_title("Contagem Mensal pelas 3 Prioridades mais Frequentes", fontsize=14)
ax.set_xlabel("Mês de Criação", fontsize=12)
ax.set_ylabel("Quantidade de Issues", fontsize=12)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
ax.grid(True, linestyle=':', alpha=0.7)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()