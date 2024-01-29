import sys
import os
from dash import Dash, dcc, html
location = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, location)
from layout import main_page, side_bar
import ids, styles, defaults
import dash_handler as dh

side_bar = html.Div([
    html.Div(className='row', children=[
        dh.input(name='SALARY', id=ids.IN_SALARY_1, value=defaults.SALARY1, style=styles.SIDEBAR),
        dh.input(name='SALARY_2', id=ids.IN_SALARY_2, value=defaults.SALARY2, style=styles.SIDEBAR),
        dh.input(name='Savings_1', id=ids.IN_SAVINGS_1, value=defaults.SAVINGS, style=styles.SIDEBAR),
        dh.dropdown(name="Year", id=ids.DD_YEAR_FIXED, value=2023, options=[2023, 2024], style=styles.SIDEBAR),
        dh.dropdown(name='RSU', id=ids.DD_RSU, value='Yes', options=["Yes", "No"], style=styles.SIDEBAR),
        html.Div(id=ids.RSU_INFO, children=[
            dh.input(name='RSU Count', id=ids.IN_RSU_1, value=defaults.RSU_COUNT),
            dh.input(name='Stock Ticker', id=ids.IN_RSU_TICKER_1, value=defaults.RSU_TICKER),
            dh.input(name='Vesting %', id=ids.IN_RSU_VESTING_1, value=defaults.RSU_PERCENT),
            dh.input(name="Vesting Term(years)", id=ids.IN_RSU_VESTING_TERM_1, value=defaults.RSU_TERM),
        ])
    ]),
    # dcc.Store(id=ids.ids.IN_SALARY_1),
    # dcc.Store(id=ids.STORE_DF_TABLE),
    # dcc.Store(id=ids.STORE_DF_PLOT),
    # dcc.Store(id=ids.STORE_LAST_DRAFTED),
    # dcc.Store(id=ids.STORE_DRAFT_PICK),
    # dcc.Store(id=ids.STORE_DRAFT_COUNT, data=0),
    # dcc.Store(id=ids.STORE_DRAFT_COUNT, data=0),
    # dcc.Store(id=ids.STORE_DRAFT_TEAM),
    # dcc.Store(id=ids.STORE_PLAYERS_AVAILABLE),
    ], style=styles.SIDEBAR_PAGE)
