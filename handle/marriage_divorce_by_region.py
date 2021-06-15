import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def make_marriage_by_region():
    df = pd.read_csv("data/marriage.csv")
    figure = go.Figure(data=[go.Pie(
        labels=df["Vùng"],
        values=df["Số lượng"],
        direction='clockwise',
        hole=.4,
        sort=True
    )])
    figure.update_layout(
        title='Tổng số cuộc kết hôn theo vùng năm 2019',
        title_x=0.5
    )
    return figure


def make_divorce_by_region():
    df = pd.read_csv("data/divorce.csv")

    figure = go.Figure(data=[go.Pie(
        labels=df["Vùng"],
        values=df["Số lượng"],
        direction='clockwise',
        hole=.4,
        sort=True
    )])

    figure.update_layout(
        title='Tổng số cuộc ly hôn theo vùng năm 2019',
        title_x=0.5
    )
    return figure
