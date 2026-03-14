def get_by_issn(df, issn):
    result = df[df["issn"] == issn]
    return result


def get_all_areas(df):
    return sorted(df["área de avaliação"].dropna().unique().tolist())


def get_by_area(df, area):
    result = df[df["área de avaliação"].str.contains(area, case=False, na=False)]
    result = result.sort_values("issn")
    return result


def get_by_stratum(df, stratum):
    result = df[df["estrato"] == stratum]
    result = result.sort_values("issn")
    return result

def filter_journals(df, area=None, stratum=None):
    result = df

    if area:
        result = result[result["área de avaliação"].str.contains(area, case=False, na=False)]

    if stratum:
        result = result[result["estrato"] == stratum]

    result = result.sort_values("issn")

    return result