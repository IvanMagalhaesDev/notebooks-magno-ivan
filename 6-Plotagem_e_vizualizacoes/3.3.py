import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
niveis = ['Baixa', 'Média', 'Alta', 'Crítica']
df = pd.DataFrame({
    'Priority': np.random.choice(niveis, size=200, p=[0.5, 0.3, 0.15, 0.05])
})

contagem = df['Priority'].value_counts()

plt.style.use("grayscale")
plt.figure(figsize=(8, 5))

contagem.plot(kind='bar')

plt.title('Contagem por Prioridade', fontsize=14)
plt.xlabel('Nível de Prioridade', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.style.use("default")