import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
n = 150

df = pd.DataFrame({
    "NoComments":    np.random.poisson(lam=3, size=n),
    "NoAttachments": np.random.poisson(lam=1, size=n),
    "NoCommits":     np.random.poisson(lam=5, size=n),
    "NoAuthors":     np.random.poisson(lam=2, size=n),
    "NoCommitters":  np.random.poisson(lam=2, size=n),
    "BFT":           np.random.exponential(scale=10, size=n)
})

colunas = ["NoComments", "NoAttachments", "NoCommits", "NoAuthors", "NoCommitters", "BFT"]

grafico = sns.pairplot(
    data=df[colunas],
    diag_kind="kde",
    plot_kws={'alpha': 0.6, 'color': 'steelblue'}
)

grafico.figure.suptitle("Pairplot: Correlações entre Contagens e BFT", y=1.02, fontsize=16, fontweight='bold')
plt.show()