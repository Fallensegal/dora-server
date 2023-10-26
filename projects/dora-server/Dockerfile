FROM python:3.11-slim

WORKDIR /opt/app
RUN pip install poetry==1.6.0
COPY . .
RUN poetry install
CMD ["poetry", "run", "uvicorn", "dora.survey:app", "--host=0.0.0.0", "--port=8000"]


