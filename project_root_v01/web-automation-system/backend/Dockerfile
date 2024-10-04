ARG DOCKER_REGISTRY=docker.io
FROM ${DOCKER_REGISTRY}/python:3.9-slim

ARG HTTP_PROXY
ARG CERT_FILENAME

WORKDIR /app

COPY . .

RUN if [ ! -z "${HTTP_PROXY}" ]; then  \
       pip install --proxy ${HTTP_PROXY} --cert ${CERT_FILENAME} --no-cache-dir -r requirements.txt;\
    else  \
       pip install --no-cache-dir -r requirements.txt;\
    fi

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]