from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/pink_morsel_sales.csv")

df["Date"] = pd.to_datetime(df["Date"])
df_summed = df.groupby("Date")["Sales"].sum().reset_index()

primary, secondary, font, graph = "#FFFFFF", "#0E90E6", "#000000", "#FFFFFF"

app = Dash()

def generate_figure(data):
    chart = px.line(data, x="Date", y="Sales", title="Pink Morsel Sales")
    chart.update_layout(
        plot_bgcolor=primary,
        paper_bgcolor=secondary,
        font_color=font
    )

    return chart

visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(df_summed)
)

header = html.H1(
    "Pink Morsel Sales Graph",
    id="header",
    style={
        "background-color": primary,
        "color": "#413C35",
        "border-radius": "10px"
    }
)

region_select = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "all",
    id="region",
    inline=True
)
region_wrapper = html.Div(
    [
        region_select
    ],
    style={
        "font-size": "125%"
    }
)

@app.callback(
    Output(visualization, "figure"),
    Input(region_select, "value")
)
def update_graph(region):
    if region == "all":
        data = df_summed
    else:
        data = df[df["Region"] == region]

    figure = generate_figure(data)
    return figure


app.layout = html.Div(
    [
        header,
        visualization,
        region_wrapper
    ],
    style={
        "textAlign": "center",
        "background-color": graph,
        "border-radius": "20px"
    }
)


app.run(debug=True)