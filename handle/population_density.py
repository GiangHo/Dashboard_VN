import json
import pandas as pd
import plotly.express as px


def make_population_density_figure():
    df = pd.read_csv("data/population_density.csv")

    with open('data/vn.json') as response:
        vietnam = json.load(response)

    figure = px.choropleth_mapbox(df, geojson=vietnam,
                                  color="Person/km2",
                                  locations="province",
                                  featureidkey="properties.ten_tinh",
                                  center={"lat": 16.46, "lon": 107.59},
                                  mapbox_style="carto-positron", zoom=3.7,
                                  title="Mật độ dân số việt Nam đầu năm 2019").update(layout=dict(title=dict(x=0.5)))
    return figure
