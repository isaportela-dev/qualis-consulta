# data_loader.py
# Responsável por carregar o dataset de periódicos a partir do arquivo Excel
# e retornar um DataFrame do pandas para ser utilizado na aplicação.
 
import pandas as pd

# Lê o arquivo Excel contendo o dataset Qualis
# e retorna um DataFrame do pandas
def load_data():
    file_path = "data/qualis.xlsx"

    df = pd.read_excel(file_path, engine="openpyxl")

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    return df