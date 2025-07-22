import pandas as pd
import folium
from folium.plugins import HeatMap
import webbrowser
import os

# .-.-.-.-.-.-.-.-.Load and clean data .-.-.-.-.-.-.-.
print("Loading COVID-19 data...")
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv"
try:
    df = pd.read_csv(url)
    df_clean = df.dropna(subset=['Lat', 'Long_', 'Confirmed'])
    print(f"Data loaded successfully. {len(df_clean)} valid records found.")
except Exception as e:
    print(f"Error loading data: {str(e)}")
    exit()

# .-.-.-.-..-.-.-.-Create heatmap.-.-.-.-..-.-.-.
print("Generating heatmap...")
m = folium.Map(location=[20, 0], zoom_start=2, tiles='cartodbpositron')

HeatMap(
    data=[[row['Lat'], row['Long_'], row['Confirmed']] for _, row in df_clean.iterrows()],
    radius=15,
    blur=10,
    gradient={0.1: 'blue', 0.3: 'lime', 0.5: 'yellow', 0.7: 'orange', 1: 'red'},
    max_zoom=4
).add_to(m)

# .-.-.-.-..-.-.-.Add title.-.-.-.-..-.-.-.
title_html = '''
    <h3 style="position:absolute; top:10px; left:50px; z-index:1000; 
    background-color:rgba(255,255,255,0.7); padding:10px">
    COVID-19 Global Heatmap (Confirmed Cases)</h3>
'''
m.get_root().html.add_child(folium.Element(title_html))

# .-.-.-.-..-.-.-.Save and open.-.-.-.-..-.-.-.
output_file = 'covid_heatmap.html'
m.save(output_file)
print(f"Heatmap saved to: {os.path.abspath(output_file)}")

# .-.-.-.-..-.-.-.Try to open automatically.-.-.-.-..-.-.-.
try:
    webbrowser.open('file://' + os.path.abspath(output_file))
    print("Opening in default browser...")
except:
    print("Could not open automatically. Please open the HTML file manually.")