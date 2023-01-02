FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV APP_MODULE main_app:app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY ./ /app