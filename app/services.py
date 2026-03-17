# services.py
# Este módulo concentra a lógica de consulta e filtragem dos dados.
# As funções aqui manipulam o DataFrame carregado do dataset.
 
# Busca um periódico específico pelo ISSN
def get_by_issn(df, issn):
    result = df[df["issn"] == issn]
    return result

# Retorna a lista de áreas de avaliação disponíveis no dataset
def get_all_areas(df):
    return sorted(df["área de avaliação"].dropna().unique().tolist())

# Retorna todos os periódicos pertencentes a uma área de avaliação
def get_by_area(df, area):
    result = df[df["área de avaliação"].str.contains(area, case=False, na=False)]
    result = result.sort_values("issn")
    return result

# Retorna periódicos que pertencem a um determinado estrato Qualis
def get_by_stratum(df, stratum):
    result = df[df["estrato"] == stratum]
    result = result.sort_values("issn")
    return result

# Aplica filtros combinados de área e estrato no dataset
# Ambos os parâmetros são opcionais
def filter_journals(df, area=None, stratum=None):
    result = df

    if area:
        result = result[result["área de avaliação"].str.contains(area, case=False, na=False)]

    if stratum:
        result = result[result["estrato"] == stratum]

    result = result.sort_values("issn")

    return result

# Calcula a quantidade de periódicos em cada estrato
# Retorna um dicionário usado para gerar o gráfico
def get_stratum_distribution(df):
    return df["estrato"].value_counts().sort_index().to_dict()