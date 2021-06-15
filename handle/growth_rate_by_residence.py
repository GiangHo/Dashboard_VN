import pandas as pd
import plotly.express as px


def make_growth_rate_by_residence_figure():
    df = pd.read_csv("data/growth_rate.csv")
    figure = px.line(df, x="Năm", y="Tỷ lệ tăng", color='Vùng')
    figure.update_layout(title='Tỷ lệ tăng dân số theo vùng', title_x=0.5)
    return figure
