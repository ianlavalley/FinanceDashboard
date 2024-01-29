from dash import Dash, dcc, html, Input, Output, dash_table, State
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import time
from typing import Sequence, Dict, Any
from pathlib import Path
import sys
location = str(Path(__file__).parents[2])
sys.path.insert(0, location)
from layout.main_page import main_page
from layout.side_bar import side_bar
import dash_handler as dh
from taxes.Get_taxes import GetTaxes
gt =GetTaxes(180000)
from taxes.income import Income
import ids, styles
from plotting import line


class DataHandler:
    def __init__(self):
        pass

    @staticmethod
    def sort_data(df, sort1: str, sort2: str = '', sort_b1: bool = False, sort_b2: bool = False) -> pd.DataFrame:
        if sort_b2:
            return df.sort_values(by=[sort1, sort2], ascending=[sort_b1, sort_b2])
        else:
            return df.sort_values(by=sort1, ascending=sort_b1)
    
    @classmethod
    def to_records(cls, df: pd.DataFrame, index_name: str=None) -> Sequence[Dict[Any, Any]]:
        if index_name:
            df[index_name] = df.index
        return df.to_dict('records')
    
    @classmethod
    def from_records(cls, df: Dict[Any, Any]) -> pd.DataFrame:
        return pd.DataFrame.from_records(df)


# ======================================================================
app = Dash(external_stylesheets=[dbc.themes.LUX])
app.layout = html.Div([
    side_bar,
    dcc.Tabs([
        dcc.Tab(label='Home Buying', children=[
            main_page,
        ]),
    ])
], style=styles.CONTENT_PAGE)
# app.layout = html.Div([dcc.Location(id="url"),side_bar, content])
# ==============================================================================================

@app.callback(
    Output(ids.IN_RSU_1, 'value'),
    Output(ids.IN_RSU_VESTING_1, 'value'),
    Output(ids.IN_RSU_TICKER_1, 'value'),
    Output(ids.IN_RSU_VESTING_TERM_1, 'value'),
    Input(ids.DD_RSU, "value"),
    prevent_initial_call=True
)
def get_rsu_info(rsus: Any):
    rsus = True if rsus == 'Yes' else False
    if rsus:
        disabled = False
    else:
        disabled = True
    return 0, 0, 'GOOG', 0


@app.callback(
    Output(ids.TAX_RESULTS, "children"),
    Input(ids.BUTTON_TAX, 'n_clicks'),
    State(ids.IN_SALARY_1, "value"),
    State(ids.IN_SALARY_2, 'value'),
    State(ids.IN_SAVINGS_1, 'value'),
    State(ids.IN_RSU_1, 'value'),
    State(ids.IN_RSU_TICKER_1, 'value'),
    State(ids.IN_RSU_VESTING_TERM_1, 'value'),
    State(ids.DD_YEAR_FIXED, 'value'),
)
def get_tax_info(n_clicks, salary, salary2, savings1, rsu_count, rsu_ticker, rsu_term, year):
    income = Income(salary=float(salary),
                    savings=savings1,
                    rsu_count=rsu_count,
                    rsu_ticker=rsu_ticker,
                    rsu_term=rsu_term)
    print(income.total_income)
    salaries = [income.total_income]
    print(salaries)
    if salary2:
        salaries.append(float(salary2))
    taxes = GetTaxes(salaries[0], year=year)
    taxes.df = taxes.df.round(2)
    # df = taxes.df.loc[[taxes.data.recommendation]]
    taxes.df["Filing Type"] = taxes.df.index
    # print("Transpose", taxes.df.T.loc[['Total Taxes', 'After-tax Income']])
    fig_tax = line.render_bar(taxes.df, 
                              x_name = taxes.df.index,
                              y_name=["Total Taxes", "After-tax Income"],
                              title=f"File {taxes.data.recommendation} - Income: ${np.sum(salaries)} - Savings: ${taxes.data.savings} - Eff_Tax: {taxes.data.eff_taxes}%")
    print(taxes.data.summary_table)

    return html.Div(children=[
        dcc.Graph(ids.GRAPH_TAX, figure=fig_tax),
        dh.table(id=ids.TABLE_SUMMARY, df=taxes.data.summary_table.round(2), style={'padding': '1rem'}),
        dh.table(id=ids.TABLE_TAX, df=taxes.df, style={'padding': '1rem'}),
    ])




app.run_server(debug=True)
