from fastapi import FastAPI
from app.routes import router
from app.utils.logging_config import setup_logging
import logging

setup_logging()

app = FastAPI()

@app.get("/")
def read_root():
    logging.info("Root endpoint was accessed")
    return {"message": "Welcome to the Web Automation System!"}
app.include_router(router)