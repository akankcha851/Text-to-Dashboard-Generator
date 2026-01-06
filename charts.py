# import plotly.express as px

# def generate_chart(chart_config, df):
#     """
#     Generates a Plotly chart based on chart configuration and dataframe.
#     """
#     chart_type = chart_config.get("type")

#     if chart_type == "bar":
#         return px.bar(df, x=chart_config["x"], y=chart_config["y"])

#     if chart_type == "line":
#         return px.line(df, x=chart_config["x"], y=chart_config["y"])

#     if chart_type == "pie":
#         return px.pie(df, names=chart_config["x"], values=chart_config["y"])

#     return None

import plotly.express as px

def generate_chart(chart_type, x_col, y_col, df):
    if x_col not in df.columns or y_col not in df.columns:
        return None

    if chart_type == "bar":
        return px.bar(df, x=x_col, y=y_col)

    if chart_type == "line":
        return px.line(df, x=x_col, y=y_col)

    if chart_type == "pie":
        return px.pie(df, names=x_col, values=y_col)

    return None


