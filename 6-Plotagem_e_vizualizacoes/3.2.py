import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    'NoComments':    np.random.poisson(lam=3, size=200),
    'NoAttachments': np.random.poisson(lam=1, size=200)
})

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5), sharex=True, sharey=True)

axes[0].hist(df['NoComments'], bins=10, alpha=0.7, color='skyblue', edgecolor='black')
axes[0].set_title('Distribuição de Comentários')
axes[0].set_xlabel('Número de Comentários')
axes[0].set_ylabel('Frequência')

axes[1].hist(df['NoAttachments'], bins=10, alpha=0.7, color='lightcoral', edgecolor='black')
axes[1].set_title('Distribuição de Anexos')
axes[1].set_xlabel('Número de Anexos')

plt.suptitle('Subplots: Distribuição de Interações', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()