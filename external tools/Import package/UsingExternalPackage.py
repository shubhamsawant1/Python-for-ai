#After installation, import and use:
# web requests 
import requests

response = requests.get("https://api.example.com/data")

# Data analysis 

import pandas as pd

# Create a simple dataFrame

data = {
  'name': ['Alice', 'Bob', 'Charlie'],
  'age': [25, 30, 35],
  'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

#! Always use virtual environments for projects. They prevent package conflicts bwtween different projects. 