FROM python:3.7.10-slim

WORKDIR /code

# Install deps
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install

# Copy code
COPY . .

CMD ["/bin/bash", "-c", "poetry run gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker app:app -w 4"]
