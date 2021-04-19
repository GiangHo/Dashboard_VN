import pandas as pd
import plotly.graph_objects as go


def make_sex_ratio_figure():
    df = pd.read_csv("../data/Ty_so_gioi_tinh_sinh.csv")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df["Năm"],
        y=df["Thành thị"],
        name='Thành thị'
    ))
    fig.add_trace(go.Bar(
        x=df["Năm"],
        y=df["Nông thôn"],
        name='Nông thôn'
    ))

    fig.update_layout(barmode='group', xaxis_tickangle=-45)
    fig.show()


def make_sex_ratio_population_figure():
    df = pd.read_csv("../data/ty_so_gioi_tinh_dan_so.csv")

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df["Năm"],
        y=df["Thành thị"],
        name='Thành thị'
    ))
    fig.add_trace(go.Bar(
        x=df["Năm"],
        y=df["Nông thôn"],
        name='Nông thôn'
    ))

    fig.update_layout(barmode='group', xaxis_tickangle=-45)
    fig.show()


if __name__ == '__main__':
    make_sex_ratio_population_figure()
