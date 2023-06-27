import os
import pandas as pd

def read_dataframe(
    filename: str
):
    if filename.endswith('.xlsx'):
        return pd.read_excel(filename)
    raise NotImplementedError('only supports xlsx document')