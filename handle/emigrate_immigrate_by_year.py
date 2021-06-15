import pandas as pd
import plotly.graph_objects as go


def make_emigrate_immigrate_figure():
    df = pd.read_csv("data/emigrate_immigrate_ratio.csv")
    figure = go.Figure(data=[
        go.Bar(name='Nhập cư', y=df["Năm"], x=df["Tỷ suất nhập cư"], orientation='h'),
        go.Bar(name='Xuất cư', y=df["Năm"], x=df["Tỷ suất xuất cư"], orientation='h')
    ])
    figure.update_layout(barmode='group', title='Tỷ suất nhập cư và xuất cư', title_x=0.5)
    return figure
