import dash
from dash import html, dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np
import os
import Mining as mg

mg.SortData.init_dataframe()
print(mg.SortData.df)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
TITLE = 'Supermarkt Verkäufe'
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
                            {'label':i, 'value':i } for i in ["Jan", "Feb", "Mär"]],
                            value = 'Feb',)
                        ]),
                        dbc.Col([
                            html.H6('Referenzmonat'),
                            dcc.Dropdown( id = 'dropdown_comp', options = [
                            {'label':i, 'value':i } for i in ["Jan", "Feb", "Mär"]],
                            value = 'Jan',)
                            ]
                        ),
                    ])
                ]
            )
        ], style={'height':'150px'})],width = 4),
        dbc.Col([dcc.Markdown("# Umsatz  aller   Mohnate: **" + mg.SortData.get_gesamtumsatz() + "€**")]),
        dbc.Col([dcc.Markdown("# Umsatz aktueller Mohnat: **" + mg.SortData.get_umsatz_im_mohnat(0) + "€**")])
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


@app.callback([Output('card_num1', 'children'),
               Output('card_num2', 'children'),
               ],)
def update_cards():
    card_content = [
        dbc.CardBody([
                html.H6('Gesamtumsatz', style = {'fontWeight':'lighter', 'textAlign':'center'}),
                html.H3('{0}{1}'.format(mg.SortData.get_gesamtumsatz(), "€"), style = {'color':'#090059','textAlign':'center'})
                ]
            )
        ]
    card_content1 = [
        dbc.CardBody([
                html.H6('Ferienumsatz', style = {'fontWeight':'lighter', 'textAlign':'center'}),
                html.H3('{0}{1}'.format(mg.SortData.get_umsatz_im_mohnat(0), "€"), style = {'color':'#090059','textAlign':'center'})
                ]
            )
        ]
    return card_content, card_content1

if __name__ == "__main__":
    app.run_server()
    # https://www.youtube.com/watch?v=cCRF7iM-iF4&list=PLh3I780jNsiTnCs2LNt4ckbV-c2HatCFg&index=2