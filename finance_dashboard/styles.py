SIDEBAR_PAGE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "17rem",
    "padding": "2rem 1rem",
    "background-color": "#D9E3F1",
    'border': "2px #FF7F7F solid",

}

RIGHT_STYLE = {
    "position": "fixed",
    "top": 0,
    "right": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "2rem 1rem",
    "background-color": "#D9E3F1",
    'border': "2px #FF7F7F solid",
}

CONTENT_PAGE = {
    "margin-left": "19rem",
    "margin-right": "0rem",
    "padding": "0rem 1rem",
}

HOVER_STYLE = {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }

SIDEBAR = {
    'padding': '.3rem 1rem',
}

DROPDOWN = {
    'padding' : '.5rem 0px', 
    'width': '99%'}

INPUT = {
    'padding': '.5rem 0px',
    'width': '99%'}

MAIN = {'width': '24%', 'padding': '0rem 0.5rem'}
# table = dash_table.DataTable(
#             id='table-dropdown',
#             data=df.to_dict('records'),
#             columns=[
#                 {'id': 'Income', 'name': 'Income'},
#                 {'id': 'Savings', 'name': 'Savings'},
#                 {'id': 'RSU_current', 'name': 'RSU_current'},
#                 {'id': 'Rsu', 'name': 'Rsu'},
#                 {'id': 'Rsu_ticker', 'name': 'Rsu_ticker'},
#                 {'id': 'Rsu_vesting_schedule', 'name': 'RSU_vesting_schedule', 'presentation': 'dropdown'},
#             ],
#
#             editable=True,
#             row_deletable=True,
#             dropdown={
#                 'Rsu_vesting_scehdule': {
#                     'options': [
#                         {'label': i, 'value': i}
#                         for i in ['33,33,22,11', '25,25,25,25']
#                     ]
#                 },
#            }