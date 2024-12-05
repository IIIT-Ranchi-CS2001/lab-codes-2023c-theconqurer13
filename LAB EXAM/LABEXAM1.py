import pandas as pd
import numpy as np
aqi_data = pd.read_csv('AQI_Data.csv')
# Display the first 8 rows
print(aqi_data.head(8))
#Display the last 5 rows
print(aqi_data.tail(5))
#Showing dtype and number of non null values 
print(aqi_data.info())
#computing mean max and min
aqi_data['AQI'] = pd.to_numeric(aqi_data['AQI'], errors='coerce')
aqi_data['PM2.5'] = pd.to_numeric(aqi_data['PM2.5'], errors='coerce')
aqi_data['PM10'] = pd.to_numeric(aqi_data['PM10'], errors='coerce')

mean_aqi = np.mean(aqi_data['AQI'])
max_pm25 = np.max(aqi_data['PM2.5'])
min_pm10 = np.min(aqi_data['PM10'])
#print the results
print("Mean AQI: ", mean_aqi)
print("Max PM2.5: ", max_pm25)
print("Min PM10: ", min_pm10)