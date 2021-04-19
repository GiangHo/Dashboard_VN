import json
import pandas as pd
import plotly.express as px


def make_growth_rate_by_residence_figure():
    df = pd.read_csv("data/Ty_le_tang_theo_vung.csv")
    figure = px.line(df, x="Năm", y="Tỷ lệ tăng", color='Vùng')
    return figure
