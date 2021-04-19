import dash as dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from handle.growth_rate_by_residence import make_growth_rate_by_residence_figure
from handle.population_density_graph import make_population_density_figure

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    html.Div(children='''
        Population of Vietnam.
    '''),
    html.Div(
        [
            html.Div(
                dcc.Graph(
                    id='province_graph',
                    figure=make_population_density_figure()
                )
            ),
            html.Div(
                dcc.Graph(
                    id='growth_rate_graph',
                    figure=make_growth_rate_by_residence_figure()
                )
            )
        ],
        style={"display": "flex"}
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)

