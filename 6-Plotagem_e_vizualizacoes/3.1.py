import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
datas_aleatorias = pd.date_range(start='2023-01-01', end='2023-12-31', periods=150)
df = pd.DataFrame({'CreationDate': datas_aleatorias, 'IssueID': range(150)})

df['CreationDate'] = pd.to_datetime(df['CreationDate'])
df_idx = df.set_index('CreationDate')

issues_por_mes = df_idx.resample('ME').size()

plt.figure(figsize=(10, 6))
issues_por_mes.plot(
    drawstyle="steps-post",
    marker="o",
    rot=45,
    color='b',
    title="Criação de Issues por Mês"
)

plt.xlabel("Mês")
plt.ylabel("Quantidade de Issues Criadas")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()