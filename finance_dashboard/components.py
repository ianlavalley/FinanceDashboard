from dash import Dash, dcc, html, Input, Output, dash_table
from typing import Sequence, List, Dict
import os
import sys

location = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, location)
import styles


def add_div(func):
    def wrapper(*args, **kwargs):
        return html.Div([func(*args, **kwargs)])

    return wrapper


def dash_table_columns(data):
    return [{"name": i, "id": i} for i in data.columns]


def button(text=None, child_text='', id=None, id_text=None, padding='.2rem 0rem'):
    if id_text:
        return html.Div([
            html.Button(text, id=id, n_clicks=0),
            html.Div(id=id_text,
                     children=child_text)
        ], style={'padding': padding})
    return html.Div([
        html.Button(text, id=id, n_clicks=0),
    ], style={'padding': padding})


def dropdown(name=None, id=None, value=None, options=None, multi=False, style=styles.DROPDOWN):
    if name:
        return html.Div([
            html.H6(name),
            dcc.Dropdown(
                id=id,
                options=options,
                value=value,
                searchable=True,
                multi=multi,
                clearable=True, )],
            style=style)
    else:
        return html.Div([
            dcc.Dropdown(
                id=id,
                options=options,
                value=value,
                searchable=True,
                multi=multi,
                clearable=True, )],
            style=style)


def input(name=None, id=None, value=None, value_type=None, style=styles.INPUT):
    if name:
        return html.Div([
            html.H6(name),
            dcc.Input(id=id,
                      value=value,
                      type=value_type)
        ], style=style)
    else:
        return html.Div([
            dcc.Input(id=id,
                      value=value,
                      type=value_type)
        ], style=style)


def range_slider(id=None, min: int = 2019, max: int = 2023, step: int = 1, value: Sequence[int] = [2019, 2023],
                 marks=None, width="100%"):
    return html.Div([
        dcc.RangeSlider(id=id, min=min, max=max, step=step, value=value, marks=marks),
    ], style={'width': width,
              'margin': '.5rem 0rem'},
    )


def text(id, text='', style=None):
    if not style:
        style = {"margin": '.5rem 0rem'}
    return html.Div(id=id,
                    children=[
                        html.P(text),
                    ], style=style
                    )
