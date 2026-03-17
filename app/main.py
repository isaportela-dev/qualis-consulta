# main.py
# Arquivo principal da aplicação FastAPI.
# Responsável por inicializar a API, carregar os dados do dataset
# e definir os endpoints disponíveis para consulta.

from fastapi import FastAPI
from app.data_loader import load_data
from app.services import get_by_issn, get_all_areas, get_by_area, get_by_stratum, filter_journals, get_stratum_distribution
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# Carrega o dataset de periódicos a partir do arquivo Excel
# utilizando a função definida em data_loader.py
df = load_data()

# Endpoint raiz que renderiza a interface web (HTML)
# Utiliza o template index.html para exibir a página inicial
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint para buscar um periódico específico pelo ISSN
# Retorna as informações do periódico encontrado
@app.get("/journal/{issn}")
def get_journal(issn: str):
    result = get_by_issn(df, issn)

    return result.to_dict(orient="records")

# Endpoint que retorna todas as áreas de avaliação disponíveis no dataset
@app.get("/areas")
def list_areas():
    return get_all_areas(df)

# Endpoint para buscar periódicos por área de avaliação
# Retorna todos os periódicos pertencentes à área informada
@app.get("/journals/by-area/{area}")
def journals_by_area(area: str):
    result = get_by_area(df, area)
    return result.to_dict(orient="records")

@app.get("/journals/by-stratum/{stratum}")
def journals_by_stratum(stratum: str):
    result = get_by_stratum(df, stratum)
    return result.to_dict(orient="records")

# Endpoint que permite aplicar filtros combinados por área e/ou estrato
# Os parâmetros são opcionais
@app.get("/journals/filter")
def journals_filter(area: str = None, stratum: str = None):
    result = filter_journals(df, area, stratum)
    return result.to_dict(orient="records")

# Endpoint que retorna a distribuição de periódicos por estrato
# Utilizado para gerar o gráfico na interface web
@app.get("/stratum-distribution")
def stratum_distribution():
    return get_stratum_distribution(df)