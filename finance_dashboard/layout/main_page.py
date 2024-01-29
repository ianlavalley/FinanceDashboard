import sys
from dash import html
from pathlib import Path

location = Path(__file__).parents[2]
sys.path.insert(0, str(location))
import ids, styles, dash_handler

main_page = html.Div([
    dash_handler.button(text="Get Tax Data", id=ids.BUTTON_TAX),
    html.Div(id=ids.TAX_RESULTS, children=[
        # html.P("Hello")
    ]
    ),
    html.Div(id='table-dropdown-container'),
])
