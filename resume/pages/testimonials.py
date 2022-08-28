import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=2)

def layout():
    return html.Div([
    html.H3("People that I've had the pleasure to work with", style={'textAlign':'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Mark Gilbert', style={'textAlign': 'center'}),
            dcc.Markdown('Director of Marketing', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Adam is very professional. I really appreciate his quick response '
                         'and great teamwork. He can sell anything that has a price to it. I highly recommend him '
                         'if you want to sell stuff in Gotham City.',
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Mark Gilbert', style={'textAlign': 'center'}),
            dcc.Markdown('Director of Marketing', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Adam is very professional. I really appreciate his quick response '
                         'and great teamwork. He can sell anything that has a price to it. I highly recommend him '
                         'if you want to sell stuff in Gotham City.',
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('#### Mark Gilbert', style={'textAlign': 'center'}),
            dcc.Markdown('Director of Marketing', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Adam is very professional. I really appreciate his quick response '
                         'and great teamwork. He can sell anything that has a price to it. I highly recommend him '
                         'if you want to sell stuff in Gotham City.',
                         className='ms-3'),
        ], width=5)
    ], justify='center')
])