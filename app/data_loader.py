import pandas as pd


def load_data():
    file_path = "data/qualis.xlsx"

    df = pd.read_excel(file_path, engine="openpyxl")

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    return df