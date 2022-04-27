from flask import Flask,render_template
import folium
import pandas as pd
import webbrowser
app=Flask(__name__)
@app.route('/')
def index():
    df = pd.read_csv("members2.csv")
    # add marker one by one on the map
    map = folium.Map(location=[28, 84], tiles="OpenStreetMap", zoom_start=7)
    for i in range(len(df)):
        folium.Marker(
            location=[df.iloc[i]['latitude'], df.iloc[i]['longitude']],
            popup=df.iloc[i]['full_name'],
            # popup=df2.iloc[i]['province'],
        ).add_to(map)

    return map._repr_html_()

if __name__=="__main__":
    app.run(debug=True)