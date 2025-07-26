from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/pink_morsel_sales.csv")

df["Date"] = pd.to_datetime(df["Date"])
df_summed = df.groupby("Date")["Sales"].sum().reset_index()

    
app = Dash()

fig = px.line(df_summed, x="Date", y="Sales", title="Pink Morsel Sales Over Time")
fig.update_layout(xaxis_title="Date", yaxis_title="Sales ($)")


app.layout = html.Div(children=[
    html.H1(children="Graph for Soul Foods"),

    dcc.Graph(
        id="example-graph",
        figure=fig
    )
])

app.run(debug=True)