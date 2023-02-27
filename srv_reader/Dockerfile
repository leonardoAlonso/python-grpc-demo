FROM python:3.8-slim

WORKDIR /code
COPY ./srv_reader/requirements.txt /code/requirements.txt

RUN pip3.8 install --upgrade pip
RUN pip3.8 install -r requirements.txt

COPY ./srv_reader /code/app
COPY ./data/100_sr.csv /tmp/data/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]