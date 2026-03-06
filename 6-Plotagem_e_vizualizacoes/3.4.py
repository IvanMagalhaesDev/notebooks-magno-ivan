import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
prioridades  = ['Baixa', 'Média', 'Alta', 'Crítica']
status_lista = ['Aberto', 'Em Andamento', 'Fechado']

df = pd.DataFrame({
    'Priority': np.random.choice(prioridades, size=300),
    'Status':   np.random.choice(status_lista, size=300)
})

crosstab_perc = pd.crosstab(df['Priority'], df['Status'], normalize='index')

fig, ax = plt.subplots(figsize=(10, 6))
crosstab_perc.plot(kind='bar', stacked=True, ax=ax, colormap='viridis', edgecolor='black', alpha=0.85)

plt.title('Proporção de Status dentro de cada Prioridade', fontsize=14, pad=15)
plt.xlabel('Prioridade', fontsize=12)
plt.ylabel('Proporção (0.0 a 1.0)', fontsize=12)
plt.xticks(rotation=0)
plt.legend(title='Status', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()