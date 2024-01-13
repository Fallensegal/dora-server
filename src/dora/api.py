from pydantic import BaseModel
from pathlib import Path
from fastapi import FastAPI, Request, Form, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, Response
from dora.models import DoraMetric, DoraMetricList

HERE = Path(__file__).parent

class AccountRequestForm(BaseModel):
    name: str = Form(...)
    roles: str = Form(...)
    email: str = Form(...)
    password: str = Form(...)

app = FastAPI()
app.mount("/static", StaticFiles(directory=HERE/"static"), name="static")

templates = Jinja2Templates(directory=HERE/"templates")

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request) -> Response:
    return templates.TemplateResponse(
        name="index.html", context={"request": request, "roles": [{"value":"pm","name":"Program Manager"}, {"value":"dev","name":"Developer"}]}
    )

@app.post("/")
def say_thankyou(name: str = Form(), roles: str = Form(), email: str = Form(), password: str = Form()) -> None:
    print(name, roles, email, password)

@app.get("/healthz")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/metrics", status_code=201)
def submit(dora_metric: DoraMetric) -> None:
    return None

@app.get("/metrics")
def get_metrics() -> DoraMetricList:
    return DoraMetricList.model_validate({
            "data":[{"user_id": "b0098d7a-b10e-44af-b61d-3e87c69c197c",
            "metric_1": 1,
            "metric_2": 2,
            "metric_3": 3,
            "metric_4": 4,
            "metric_5": 5}]
        })
