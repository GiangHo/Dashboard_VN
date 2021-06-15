import dash as dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from handle.birth_death_rate_by_year import make_birth_death_rate_figure
from handle.emigrate_immigrate_by_year import make_emigrate_immigrate_figure
from handle.growth_rate_by_residence import make_growth_rate_by_residence_figure
from handle.marriage_divorce_by_region import make_marriage_by_region, make_divorce_by_region
from handle.population_density import make_population_density_figure

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
    html.H1(children='Dashboard'),

    html.Div(children='''
        Population of Vietnam.
    '''),

    html.Div([
        html.Div([
            html.Div(
                [
                    html.P("Tổng dân số*"),
                    html.H6("96.484 nghìn người")
                ],
                className="info_statistic"
            ),
            html.Div(
                [
                    html.P("Tuổi thọ TB*"),
                    html.H6("73,6 tuổi")
                ],
                className="info_statistic"
            ),
            html.Div(
                [
                    html.P("Tỷ lệ biết chữ trên 15 tuổi*"),
                    html.H6("95,8 %")
                ],
                className="info_statistic"
            ),
            html.Div(
                [
                    html.P("Tỷ số giới tính khi sinh*"),
                    html.H6("111,5 bé trai/100 bé gái")
                ],
                className="info_statistic"
            ),
            html.Div(
                [
                    html.P("Tỷ số giới tính dân số*"),
                    html.H6("99,1 nam/100 nữ")
                ],
                className="info_statistic"
            )

        ],
            className="info_overview",
        )
    ]),
    html.Div(children='''*Thống kê sơ bộ năm 2019'''),

    html.Div([
        html.Div(
                [
                    html.Div(
                        dcc.Graph(
                            id='province_graph',
                            figure=make_population_density_figure()
                        ),
                        className="figure_overview",
                    ),
                    html.Div(
                        dcc.Graph(
                            id='growth_rate_graph',
                            figure=make_growth_rate_by_residence_figure()
                        ),
                        className="figure_overview",
                    )
                ],
                style={"display": "flex"}
        ),
        html.Div(
                [
                    html.Div(
                        dcc.Graph(
                            id='birth_death_rate_by_year',
                            figure=make_birth_death_rate_figure()
                        ),
                        className="figure_overview",
                    ),
                    html.Div(
                        dcc.Graph(
                            id='emigrate_immigrate_by_year',
                            figure=make_emigrate_immigrate_figure()
                        ),
                        className="figure_overview",
                    )
                ],
                style={"display": "flex"}
        ),
        html.Div(
                [
                    html.Div(
                        dcc.Graph(
                            id='marriage',
                            figure=make_marriage_by_region()
                        ),
                        className="figure_overview",
                    ),
                    html.Div(
                        dcc.Graph(
                            id='divorce',
                            figure=make_divorce_by_region()
                        ),
                        className="figure_overview",
                    )
                ],
                style={"display": "flex"}
        ),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True)

