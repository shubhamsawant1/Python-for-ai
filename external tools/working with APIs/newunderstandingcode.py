
import requests
import pandas as pd
from datetime import datetime, timedelta

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Historical weather API
url = (
    "https://archive-api.open-meteo.com/v1/archive"
    f"?latitude=48.85&longitude=2.35"
    f"&start_date={start_date}"
    f"&end_date={end_date}"
    "&daily=temperature_2m_max,temperature_2m_min"
    "&timezone=Europe/Paris"
)

# Get API response
response = requests.get(url, timeout=30)
response.raise_for_status()
data = response.json()

# Extract daily data
daily_data = data["daily"]

# Create DataFrame
df = pd.DataFrame({
    "date": daily_data["time"],
    "max_temp": daily_data["temperature_2m_max"],
    "min_temp": daily_data["temperature_2m_min"]
})

# Convert date strings into datetime
df["date"] = pd.to_datetime(df["date"])

print(df)
