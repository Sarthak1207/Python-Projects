import pandas as pd

a = pd.read_csv("First.csv")
b = pd.read_csv("Second.csv")
b = b.dropna(axis=1)
merged = a.merge(b, on='group')
merged.to_csv("output.csv", index=False)
