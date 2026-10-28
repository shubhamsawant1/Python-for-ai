import pandas as pd

df = pd.read_csv("transaction.csv")
# print(df)
# print(df.head(5))
# print(f"shape of df: {df.shape}")
# print(df.head(1))
# print(df.shape)
# print(df.groupby("type").sum())
# print(df.cumsum())

dfStudent = pd.read_csv("names.csv")
print(dfStudent.head(4))

# print(dfStudent[dfStudent["age"] > 22])
# print(dfStudent["age"].mean())
# print(dfStudent["age"].max())
# print(dfStudent["student"].value_counts())
# print(dfStudent[dfStudent["degree"] == "Bachelor"])
# print(dfStudent[dfStudent["degree"] == "Master"])
# print(dfStudent[dfStudent["age"] > 22][["name", "age"]])
# print(dfStudent[dfStudent["age"] > 22][["name", "age"]].sort_index(ascending=False))

print(dfStudent[dfStudent["name"].str.startswith("s")])
print(dfStudent[dfStudent["name"].str.endswith("h")])
print(dfStudent[dfStudent["name"].str.contains("a")])