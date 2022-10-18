import dash
from dash import html, dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np
import os
import Mining as mg
import plotly.express as px

mg.SortData.init_dataframe()
print(mg.SortData.df)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
TITLE = 'Supermarkt Verkäufe'
MONTHS = ["Gesammt", "Jan", "Feb", "Mär"]
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
    html.Br(),
    ],
    style = {'backgroundColor':'#f7f7f7'}, fluid = True
    )
app.layout = html.Div(id = 'parent', children = [navbar, body_app])
@app.callback([Output('gesamtumsatz', 'srcDoc'), 
               Output('mohnatlicher_umsatz', 'srcDoc'),
               Output('card_num3', 'children'),
               Output('card_num4', 'children'),
               Output('card_num5', 'children'),
               Output('card_num6', 'children'),
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
    print("Base: ", base, "Comp: ", comparison)
    result_0 = "Umsatz Basis  Mohnat: " + mg.SortData.get_umsatz_im_mohnat(months_index) + "€"
    result_1 = "Umsatz Referenzmonat: " + mg.SortData.get_umsatz_im_mohnat(motnhs_index_comp) + "€"
    data_2_base = mg.SortData.umsatz_nach_filialen(months_index)
    data_2_comp = mg.SortData.umsatz_nach_filialen(motnhs_index_comp)
    result_2 = [
         dbc.CardBody([
                 html.H6('Umsatz nach Filiale Base', 
                 style = {'fontWeight':'bold', 'textAlign':'center'}),
                 dcc.Graph(figure = px.bar(x = data_2_base["Filiale"], y = data_2_base["Gesamtpreis"]))
                 ]
             )
         ]
    result_2_1 = [
         dbc.CardBody([
                 html.H6('Umsatz nach Filiale Referenzmonat', 
                 style = {'fontWeight':'bold', 'textAlign':'center'}),
                 dcc.Graph(figure = px.bar(x = data_2_comp["Filiale"], y = data_2_comp["Gesamtpreis"]))
                 ]
             )
         ]
    data_3_base = mg.SortData.umsatz_nach_geschlecht(months_index)
    data_3_comp = mg.SortData.umsatz_nach_geschlecht(motnhs_index_comp)
    result_3 = [
         dbc.CardBody([
                 html.H6('Umsatz nach Geschlecht Base', 
                 style = {'fontWeight':'bold', 'textAlign':'center'}),
                 dcc.Graph(figure = px.pie(names = data_3_base["Geschlecht"], values = data_3_base["Gesamtpreis"]))
                 ]
             )
         ]
    result_3_1 = [
         dbc.CardBody([
                 html.H6('Umsatz nach Geschlecht Referenzmonat', 
                 style = {'fontWeight':'bold', 'textAlign':'center'}),
                 dcc.Graph(figure = px.pie(names = data_3_comp["Geschlecht"], values = data_3_comp["Gesamtpreis"]))
                 ]
             )
         ]
    return result_0, result_1, result_2, result_2_1, result_3, result_3_1

if __name__ == "__main__":
    app.run_server()