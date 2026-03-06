import pandas as pd
import numpy as np
from IPython.display import display

s_a = pd.Series([np.nan, 2.5, 0.0, np.nan], index=list("abcd"))
s_b = pd.Series([0.0, np.nan, 2.0, 5.0], index=list("acde"))

df1 = pd.DataFrame(
    {"A": [1.0, np.nan, 5.0, np.nan], "B": [np.nan, 2.0, np.nan, 6.0]},
    index=list("abcd")
)
df2 = pd.DataFrame(
    {"A": [5.0, 4.0, np.nan], "B": [np.nan, 3.0, 4.0]},
    index=list("bcd")
)

print("combine_first em Series:")
display(s_a.combine_first(s_b))

print("combine_first em DataFrames:")
display(df1.combine_first(df2))

print("combine_first apenas na coluna 'A':")
display(df1[["A"]].combine_first(df2))