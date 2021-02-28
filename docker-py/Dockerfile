# set base image (host OS)
FROM python:3.8

# install pipenv
RUN pip install pipenv

WORKDIR /code

COPY Pipfile Pipfile.lock .

RUN pipenv install --system --deploy

COPY src/ ./src/ 

ENV FLASK_APP=/code/src/server.py
ENV FLASK_ENV=development
CMD [ "flask", "run", "--host=0.0.0.0"  ]
