import plotly.express as px


def render_line(df, x_name, y_name, hue=None, title=None):
    return px.line(data_frame=df, x=x_name, y=y_name, color=hue, title=title)


def render_scatter(df, x_name, y_name, hue=None, title=None):
    return px.scatter(data_frame=df, x=x_name, y=y_name, color=hue, title=title)


def render_bar(df, x_name, y_name, color=None, title=None):
    return px.bar(data_frame=df, x=x_name, y=y_name, color=color, title=title, barmode='group')
