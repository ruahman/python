from python:3.10.0 as dev
WORKDIR /code
COPY pyproject.toml .
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
EXPOSE 5000
COPY . .
CMD ["bash"]
