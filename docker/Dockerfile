FROM python:3.8

EXPOSE 8000

WORKDIR /code

RUN pip install pipenv

COPY Pipfile* .

# dev
RUN pipenv install

# deploy
# RUN pipenv install --system --deploy
