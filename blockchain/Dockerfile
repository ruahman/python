from python:3.10.0
WORKDIR /code
COPY pyproject.toml .
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
# RUN poetry install --no-dev
