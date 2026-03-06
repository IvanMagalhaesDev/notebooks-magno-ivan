import pandas as pd
import numpy as np
from IPython.display import display

s1 = pd.Series([0, 1], index=["a", "b"])
s2 = pd.Series([2, 3, 4], index=["c", "d", "e"])
s3 = pd.Series([5, 6], index=["e", "f"])

df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=list("abc"), columns=["x", "y"])
df2 = pd.DataFrame(np.arange(4).reshape(2, 2) + 10, index=list("ac"), columns=["y", "z"])

print("Concat Series (axis=0):")
display(pd.concat([s1, s2, s3], axis=0))

print("Concat Series nas colunas com join='inner':")
display(pd.concat([s1, s2, s3], axis="columns", join="inner"))

print("Concat DataFrames nas colunas com keys:")
display(pd.concat([df1, df2], axis="columns", keys=["L", "R"], names=["blk", "col"]))

print("Concat DataFrames nas linhas com ignore_index=True:")
display(pd.concat([df1, df2], axis=0, ignore_index=True))