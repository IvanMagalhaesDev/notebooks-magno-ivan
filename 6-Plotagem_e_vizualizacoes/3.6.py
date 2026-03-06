import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
n = 150

no_comments = np.random.poisson(lam=5, size=n)
bft = no_comments * 3.5 + np.random.normal(loc=10, scale=8, size=n)

df = pd.DataFrame({
    'Key':        [f"BUG-{i}" for i in range(1, n + 1)],
    'NoComments': no_comments,
    'BFT':        bft
})
df.loc[0:5, 'BFT'] = 0

p95 = df['BFT'].quantile(0.95)
df_filtrado = df[(df['BFT'] > 0) & (df['BFT'] <= p95)].copy()

plt.figure(figsize=(10, 6))
sns.regplot(
    data=df_filtrado,
    x='NoComments',
    y='BFT',
    scatter_kws={'alpha': 0.6, 'color': 'steelblue'},
    line_kws={'color': 'red', 'linewidth': 2}
)

top_3 = df_filtrado.nlargest(3, 'BFT')
for _, row in top_3.iterrows():
    plt.annotate(
        text=row['Key'],
        xy=(row['NoComments'], row['BFT']),
        xytext=(0, 10),
        textcoords="offset points",
        ha='center',
        fontsize=9,
        fontweight='bold',
        color='darkred'
    )

plt.title(f'Dispersão e Regressão: NoComments x BFT\n(BFT > 0 e <= p95 [{p95:.2f}])', fontsize=14)
plt.xlabel('Número de Comentários (NoComments)', fontsize=12)
plt.ylabel('Bug Fixing Time (BFT)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()