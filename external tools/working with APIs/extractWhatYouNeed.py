
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Extract weather information
def get_weather(latitude, longitude):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
    )

    response.raise_for_status()
    data = response.json()

    return data['current']['temperature_2m']


# Get temperatures for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")


# Create sample weather data
data = {
    'date': [
        'Nov 10', 'Nov 11', 'Nov 12',
        'Nov 13', 'Nov 14', 'Nov 15', 'Nov 16'
    ],
    'max_temp': [25, 27, 23, 26, 28, 24, 26],
    'min_temp': [16, 17, 15, 18, 19, 16, 17]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)


# Create the plot
plt.figure(figsize=(6, 6))

plt.plot(df['date'], df['max_temp'],
         marker='o', label='Max Temp')

plt.plot(df['date'], df['min_temp'],
         marker='o', label='Min Temp')


# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('London Weather - Past 7 Days')
plt.legend()

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Paris Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels
plt.xticks(rotation=45)
plt.tight_layout()

# Save and display
plt.savefig('weather_chart.png')
plt.show()
      