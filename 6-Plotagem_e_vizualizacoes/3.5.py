import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
tempos_normais = np.random.exponential(scale=10, size=500)
outliers = np.random.uniform(100, 300, size=20)

df = pd.DataFrame({'BFT': np.concatenate([tempos_normais, outliers])})

p95 = df['BFT'].quantile(0.95)
df_filtrado = df[df['BFT'] <= p95]

plt.figure(figsize=(10, 6))
sns.histplot(
    data=df_filtrado,
    x='BFT',
    kde=True,
    stat='density',
    color='purple',
    bins=25
)

plt.title(f'Distribuição do Tempo de Resolução (BFT)\n(limite p95 = {p95:.2f})', fontsize=14)
plt.xlabel('Bug Fixing Time (BFT)', fontsize=12)
plt.ylabel('Densidade', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()