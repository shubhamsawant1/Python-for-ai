# Extract what you need
""" Now you can pull out specific informaction: """
import requests

def get_weather(latitude, longitude):
  response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
  data = response.json()
  return data['current']['temperature_2m']

# Get temperature for different cities

paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")

import matplotlib.pyplot as plt

# Create the plot

plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

# Add labels and title

plt.xlabel('Date')
plt.ylabel('Temperature (c)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotiation=45)
plt.tight_layout()

# Save the plot

plt.savefig('weather_chart.png')
plt.show()
      