from fastapi import FastAPI
from app.data_loader import load_data
from app.services import get_by_issn, get_all_areas, get_by_area, get_by_stratum, filter_journals
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

df = load_data()


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/journal/{issn}")
def get_journal(issn: str):
    result = get_by_issn(df, issn)

    return result.to_dict(orient="records")

@app.get("/areas")
def list_areas():
    return get_all_areas(df)

@app.get("/journals/by-area/{area}")
def journals_by_area(area: str):
    result = get_by_area(df, area)
    return result.to_dict(orient="records")

@app.get("/journals/by-stratum/{stratum}")
def journals_by_stratum(stratum: str):
    result = get_by_stratum(df, stratum)
    return result.to_dict(orient="records")

@app.get("/journals/filter")
def journals_filter(area: str = None, stratum: str = None):
    result = filter_journals(df, area, stratum)
    return result.to_dict(orient="records")