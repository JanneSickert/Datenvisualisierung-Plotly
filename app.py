import dash
from dash import html, dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np
import os
import Mining as mg
import MiningGesamt

mg.SortData.init_dataframe()
print(mg.SortData.df)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
TITLE = 'Supermarkt Verkäufe'
MONTHS = ["Jan", "Feb", "Mär"]
app.title = TITLE
server = app.server
navbar = dbc.Navbar( id = 'navbar', children = [
    dbc.Row([
        dbc.Col(html.Img(src = PLOTLY_LOGO, height = "70px")),
        dbc.Col(
            dbc.NavbarBrand(TITLE, 
            style = {'color':'white', 'fontSize':'25px','fontFamily':'Times New Roman'}))
        ],align = "center")
    ], color = '#090059')
body_app = dbc.Container([
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([dbc.Card([
            dbc.CardBody([
                    html.H6('Monate auswählen', style = {'textAlign':'center'}),
                    dbc.Row([
                        dbc.Col([
                            html.H6('Aktueller Monat'),
                            dcc.Dropdown( id = 'dropdown_base', options = [
                            {'label':i, 'value':i } for i in MONTHS],
                            value = 'Feb',)
                        ]),
                        dbc.Col([
                            html.H6('Referenzmonat'),
                            dcc.Dropdown( id = 'dropdown_comp', options = [
                            {'label':i, 'value':i } for i in MONTHS],
                            value = 'Jan',)
                            ]
                        ),
                    ])
                ]
            )
        ], style={'height':'150px'})],width = 4),
        dbc.Col(html.Iframe(
            id='gesamtumsatz',
            srcDoc=None
        )),
        dbc.Col(html.Iframe(
            id='mohnatlicher_umsatz',
            srcDoc=None
        ))
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([dbc.Card(id = 'card_num3',style={'height':'350px'})]),
        dbc.Col([dbc.Card(id = 'card_num4',style={'height':'350px'})])
        ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([dbc.Card(id = 'card_num5',style={'height':'350px'})]),
        dbc.Col([dbc.Card(id = 'card_num6',style={'height':'350px'})])
        ]),
    html.Br(),
    html.Br()
    ],
    style = {'backgroundColor':'#f7f7f7'}, fluid = True
    )
app.layout = html.Div(id = 'parent', children = [navbar, body_app])
mg.print_all()
@app.callback([Output('gesamtumsatz', 'srcDoc'), 
               Output('mohnatlicher_umsatz', 'srcDoc'),
               Output('card_num3', 'children'),
               #Output('card_num4', 'children'),
               #Output('card_num5', 'children'),
               #Output('card_num6', 'children')
               ],
              [Input('dropdown_base','value'), Input('dropdown_comp','value')])
def update_cards(base, comparison):
    months_index = 0
    motnhs_index_comp = 0
    while months_index < len(MONTHS):
        if base == MONTHS[months_index]:
            break
        else:
            months_index += 1
    while motnhs_index_comp < len(MONTHS):
        if comparison == MONTHS[motnhs_index_comp]:
            break
        else:
            motnhs_index_comp += 1
    months_index += 1
    motnhs_index_comp += 1
    print(base)
    result_0 = "Umsatz  aller   Mohnate: " + mg.SortData.get_gesamtumsatz() + "€"
    result_1 = "Umsatz aktueller Mohnat: " + mg.SortData.get_umsatz_im_mohnat(months_index) + "€"
    result_2 = [
            dbc.CardBody([
                html.H6('Umsatz nach Geschlecht', style = {'fontWeight':'bold', 'textAlign':'center'}),
                dbc.Row([
                    dbc.Col([dcc.Graph(figure = go.Bar(x = ["A", "B"], y = [22, 44], text="Umsatz der Filiale"), style = {'height':'300px'}),
                ]),
                    dbc.Col([dcc.Graph(figure = go.Bar(x = ["A", "B"], y = [22, 44], text="Umsatz der Filiale"), style = {'height':'300px'}),
                ])
                ])
            ])
    ]
    return result_0, result_1, result_2

if __name__ == "__main__":
    app.run_server()