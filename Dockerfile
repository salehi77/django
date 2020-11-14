# docker run -d --rm -p 5432:5432 -e POSTGRES_PASSWORD=password -v $HOME/Desktop/django/.venv/data:/var/lib/postgresql/data postgres:13.1-alpine

FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY Pipfile*.txt /code/
RUN pip install pipenv
RUN pipenv install
COPY . /code/