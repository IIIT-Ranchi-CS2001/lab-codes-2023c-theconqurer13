import pandas as pd
import numpy as np
aqi_data = pd.read_csv('AQI_Data.csv')
aqi_data_grouped = aqi_data.groupby('City')
#average AQi
avg_aqi = aqi_data_grouped['AQI'].mean()
#maximum PM2.5 value
max_pm25 = aqi_data_grouped['PM2.5'].max()
#minimum PM10 value
min_pm10 = aqi_data_grouped['PM10'].min()
#ptinting all three data for a specific city
result = avg_aqi.to_dict()
for city in avg_aqi.index:
    result[city] = [result[city], max_pm25[city], min_pm10[city]]

print(result)



