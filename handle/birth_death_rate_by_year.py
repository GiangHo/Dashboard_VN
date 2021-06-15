import pandas as pd
import plotly.graph_objects as go


def make_birth_death_rate_figure():
    df = pd.read_csv("data/birth_death_rate.csv")
    figure = go.Figure(data=[
        go.Bar(name='Sinh thô', x=df["Năm"], y=df["Tỷ suất sinh thô"]),
        go.Bar(name='Tử thô', x=df["Năm"], y=df["Tỷ suất chết thô"])
    ])
    figure.update_layout(barmode='stack', title='Tỷ suất sinh thô và tử thô', title_x=0.5)
    return figure
