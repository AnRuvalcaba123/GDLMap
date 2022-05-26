import folium
import pandas as pd 
import json 
from folium import plugins

df = pd.read_csv('miBiciInGDLCountry.csv')

with open('LimiteEstatal2012.geojson') as f:
    jaArea = json.load(f)

#initialize the map around Jalisco state
jaMap = folium.Map(location=[20.66682,-103.39182],titles='Stamen Toner',zoom_start=9)

##add the shape of Jalisco state to the map
folium.GeoJson(jaArea).add_to(jaMap)

#for each row in the Mibici dataset, plot the corresponding latitude and longitude on the map  
for i, row in df.iterrows():
    folium.CircleMarker((row.latitude,row.longitude), radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(jaMap)

#save the map as html
jaMap.save('jaPointMap.html')