# Page on which the players add player (the category of the game and the soberty score of the game)

import dash
# output, Input, State for callbacks
from dash import html,Output,Input,State,dcc,ctx
import dash_bootstrap_components as dbc
from Player import Player 


# Initialisation of the page style
external_stylesheets=[dbc.themes.SPACELAB]

# Creation of the web app with dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Start the server on with the app will run
server = app.server

# html.Div creates a container for other HTML elements, className indicates the style of the Div based on the page style initialised previously "external_stylesheets"
# html.H3 creates a level 3 heading element in HTML, style is to create the style of this header, here centered
Menu = html.Div(
    [
        html.H3('My Game',style={'textAlign': 'center'})
        ],    
    className="my-3",
)

# Put the Menu (the title) into a black bar at the top of the page
navbar = dbc.Navbar(
    dbc.Container(
        [
            Menu,
        ]
    ),
    color='#111111',
    dark=True,
)

# Input box to add the name of a new player, id : player-input
player_input = html.Div(
    [
        dcc.Input(id="player-input", type="text", value = '',placeholder=""),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)

# Confirmation button to add a player to the game
button_add = html.Div(
    [
        dbc.Button("Add",id = 'add',type = 'submit',color="success"),
    ],
    className="d-grid gap-1 col-2 mx-auto",
)

# Button to start the game, id : start-game
start_button = html.Div(
    [
        dbc.Button("Show Final Rules",id = 'start-game',type = 'submit',color="primary"),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)

space = '''
###
'''


#Callback : he callback function is executed whenever one or more input values change, 
# and it generates new output values that are sent to one or more output components in the layout.
@app.callback(
    Output('output-player',"children"),
    [Input('add','n_clicks')],
    [State("player-input", "value")])
def add_box(n_clicks, name):
    if n_clicks is not None:
        player = Player(name,0)
        list.list_players.append(player)
    return list.__repr__()


Player_output = html.Div(
                id = 'output-player',
                className="d-grid gap-2 col-4 mx-auto"),

# Layout of the webapp, every element that should be in the web app is added here, this is going to be the final layout of the app
# dbc.Row makes possible that each element in the container is added one bellow each other

txt_player = html.Div(id='output-player',children=[])

from ListPlayer import ListPlayer

list = ListPlayer([])
"""
list_joueurs = html.Div(
    [
        dcc.Markdown(id = 'output-player'),
    ],
    className="d-grid gap-2 col-4 mx-auto",
)"""

app.layout = dbc.Container([
    dbc.Row(
        [
        navbar,
        dcc.Markdown(children=space),
        player_input,
        dcc.Markdown(children=space),
        button_add,
        dcc.Markdown(children=space),
        txt_player,
        dcc.Markdown(children=space),
        start_button,
        ], align='center',className="g-0",
    )
], fluid=True)






if __name__ == "__main__":
    app.run(debug=False)
