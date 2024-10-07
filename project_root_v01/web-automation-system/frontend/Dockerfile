ARG DOCKER_REGISTRY=docker.io
FROM ${DOCKER_REGISTRY}/python:3.9-slim

ARG HTTP_PROXY
ARG CERT_FILENAME

WORKDIR /app
COPY requirements.txt requirements.txt
RUN if [ ! -z "${HTTP_PROXY}" ]; then  \
       pip install --proxy ${HTTP_PROXY} --cert ${CERT_FILENAME} --no-cache-dir -r requirements.txt;\
    else  \
       pip install --no-cache-dir -r requirements.txt;\
    fi

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]