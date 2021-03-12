FROM python:3.8

EXPOSE 8000

WORKDIR /code

RUN pip install pipenv

COPY Pipfile* .

# RUN pipenv install --system --deploy
RUN pipenv install
