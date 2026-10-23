import pandas as pd

df = pd.read_csv("transaction.csv")
print(df)
print(df.head(5))
print(f"shape of df: {df.shape}")