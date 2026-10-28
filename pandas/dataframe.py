import pandas as pd

# i want to store passenger data of the Titanic. For a number of Passengers, I know the number name (Character), age (integers) and sex (male/female) data.

df = pd.DataFrame(
  {
    "Name": [
      "braund, Mr. Owen Harris",
      "Allen, Mr. William Henry",
      "Bonnell, Miss Elizabeth"
    ],
    "Age": [22,35,55],
    "Sex": ["male", "male", "female"]
  }
)

print(df)
print(df[df["Age"] > 25])
print(df[df["Sex"] == "female"])