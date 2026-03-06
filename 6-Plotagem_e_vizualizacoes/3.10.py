import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
n = 500

devs = [f'Dev_{chr(65+i)}' for i in range(15)]

df = pd.DataFrame({
    'Type':     np.random.choice(['Bug', 'Melhoria', 'Tarefa', 'Documentação'], size=n, p=[0.5, 0.3, 0.15, 0.05]),
    'Assignee': np.random.choice(devs, size=n)
})

plt.rcParams['figure.figsize'] = (10, 5)
fig, axes = plt.subplots(nrows=1, ncols=2)

df['Type'].value_counts().plot(kind='bar', ax=axes[0], color='cornflowerblue', edgecolor='black')
axes[0].set_title('Contagem por Tipo de Issue')
axes[0].set_ylabel('Quantidade')
axes[0].tick_params(axis='x', rotation=45)

top_10 = df['Assignee'].value_counts().head(10).sort_values(ascending=True)
top_10.plot(kind='barh', ax=axes[1], color='mediumseagreen', edgecolor='black')
axes[1].set_title('Top 10 Assignees por Número de Issues')
axes[1].set_xlabel('Quantidade de Issues')

plt.tight_layout()

caminho = './bugfix_summary.png'
plt.savefig(caminho, dpi=200, bbox_inches='tight')
print(f"Gráfico salvo em: {caminho}")

plt.show()
plt.rcdefaults()