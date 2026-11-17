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
print(dfStudent.head(4)) # 0 ot 3 rows 

# print(dfStudent[dfStudent["age"] > 22])
# print(dfStudent["age"].mean())
# print(dfStudent["age"].max())
# print(dfStudent["student"].value_counts())
# print(dfStudent[dfStudent["degree"] == "Bachelor"])
# print(dfStudent[dfStudent["degree"] == "Master"])
# print(dfStudent[dfStudent["age"] > 22][["name", "age"]])
# print(dfStudent[dfStudent["age"] > 22][["name", "age"]].sort_index(ascending=False))

print(dfStudent[dfStudent["name"].str.startswith("s")]) # rows that name start with s
print(dfStudent[dfStudent["name"].str.endswith("h")]) # rows that name ends with h
print(dfStudent[dfStudent["name"].str.contains("a")]) # rows which name contain a
print(dfStudent[dfStudent["degree"].str.contains("phD")]) # rows which degree holds phd
print(dfStudent[dfStudent["salary"] > 20000] [["name", "salary"]]) # student who holds salary more than 20000
print(dfStudent[dfStudent["salary"].between(20000, 40000)]) # students who holds salary between 20000 to 40000
print(dfStudent[dfStudent["salary"]]) # print students salary
