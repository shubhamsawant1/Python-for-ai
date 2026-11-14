# Real Weather data using a free weather API:

import requests
import pandas as pd

# we need coordinates to get  weather data
latitude = 48.85 #Paries latitude
longitude = 2.35 #Paris longtitude

# Build the API URl with out parameters 


url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"


# make the request 

response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)
print(df)

# install requests - pip install requests

