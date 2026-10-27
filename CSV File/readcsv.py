import pandas as pd

df = pd.read_csv("transaction.csv")
# print(df)
# print(df.head(5))
# print(f"shape of df: {df.shape}")
print(df.head(1))
print(df.shape)
print(df.groupby("type").sum())
print(df.cumsum())

dfStudent = pd.read_csv("names.csv")
print(dfStudent.head(2))