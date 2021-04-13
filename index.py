import dash as dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import json

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


def make_province_graph_figure():
    df = pd.read_csv("data/Mat-do-dan-so.csv")

    with open('data/vn.json') as response:
        vietnam = json.load(response)

    figure = px.choropleth_mapbox(df, geojson=vietnam,
                                  color="Person/km2",
                                  locations="province",
                                  featureidkey="properties.ten_tinh",
                                  center={"lat": 16.46, "lon": 107.59},
                                  mapbox_style="carto-positron", zoom=4.7, height=800)
    return figure


app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    html.Div(children='''
        Vietnam population density.
    '''),

    dcc.Graph(
        id='province_graph',
        figure=make_province_graph_figure()
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)

