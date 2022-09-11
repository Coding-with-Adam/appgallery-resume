import dash
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from .side_bar import sidebar
import pandas as pd
import plotly.express as px

dash.register_page(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Other/Dash_Introduction/intro_bees.csv"
)

df = df.groupby(["State", "ANSI", "Affected by", "Year", "state_code"])[
    ["Pct of Colonies Impacted"]
].mean()
df.reset_index(inplace=True)

# ------------------------------------------------------------------------------
def layout():
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col([sidebar()], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),
                    dbc.Col(
                        [
                            html.H1(
                                "Python Data Apps with Dash",
                                style={"text-align": "center"},
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            dcc.Dropdown(
                                                id="slct_year",
                                                options=df.Year.unique(),
                                                value=2015,
                                                style={"color": "black"},
                                            )
                                        ],
                                        width=4,
                                    )
                                ]
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [dcc.Graph(id="my_bee_map", figure={})],
                                        width=12,
                                    )
                                ]
                            ),
                        ],
                        xs=8,
                        sm=8,
                        md=10,
                        lg=10,
                        xl=10,
                        xxl=10,
                    ),
                ]
            )
        ]
    )


# ------------------------------------------------------------------------------
@callback(
    Output(component_id="my_bee_map", component_property="figure"),
    Input(component_id="slct_year", component_property="value"),
)
def update_graph(option_slctd):

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    dff = dff[dff["Affected by"] == "Varroa_mites"]

    fig = px.choropleth(
        data_frame=dff,
        locationmode="USA-states",
        locations="state_code",
        scope="usa",
        color="Pct of Colonies Impacted",
        hover_data=["State", "Pct of Colonies Impacted"],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={"Pct of Colonies Impacted": "% of Bee Colonies"},
        template="plotly_dark",
    )

    return fig
