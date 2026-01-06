


# import pandas as pd

# def load_mock_data():
#     return pd.DataFrame({
#         "Region": ["North", "South", "East", "West"],
#         "Revenue": [120000, 95000, 105000, 110000],
#         "Month": ["Jan", "Feb", "Mar", "Apr"],
#         "Growth": [5, 7, 6, 8]
#     })

# def load_csv(uploaded_file):
#     return pd.read_csv(uploaded_file)

import pandas as pd

def load_mock_data():
    return pd.DataFrame({
        "Region": ["North", "South", "East", "West"],
        "Revenue": [120000, 95000, 105000, 110000],
        "Month": ["Jan", "Feb", "Mar", "Apr"],
        "Growth": [5, 7, 6, 8]
    })

def load_csv(uploaded_file):
    return pd.read_csv(uploaded_file)

def analyze_dataframe(df):
    """
    Automatically detect numeric and categorical columns
    """
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

    return numeric_cols, categorical_cols

