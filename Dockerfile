FROM python:3.9.13
ARG port
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

ENV PORT=$port
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT --reload