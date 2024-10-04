import os
import logging

from fastapi import APIRouter, HTTPException

from app.config import get_templates_dir
from app.models import ScreenshotRequest, EmailRequest, TemplateRequest
from app.services.screenshot_service import ScreenshotService
from app.services.email_service import EmailService
from app.utils.logging_config import setup_logging

setup_logging()
router = APIRouter()

@router.get("/templates")
def get_templates():
    try:
        templates = [f for f in os.listdir(get_templates_dir()) if f.endswith('.html')]
        return {"templates": templates}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/template/{template_name}")
def get_template(template_name: str):
    try:
        with open(os.path.join(get_templates_dir(), template_name), 'r') as file:
            content = file.read()
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/template/{template_name}")
def save_template(template_name: str, request: TemplateRequest):
    try:
        with open(os.path.join(get_templates_dir(), template_name), 'w') as file:
            file.write(request.content)
        return {"message": "Template saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/screenshot")
def screenshot(request: ScreenshotRequest):
    screenshot_service = ScreenshotService()
    try:
        results = []
        for s in request.screenshots:
            result = screenshot_service.capture_screenshot(s.id, s.url, s.width, s.height)
            results.append(result)
        return {"message": "Screenshots taken", "results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/send-email")
def email(request: EmailRequest):
    logging.info(f"Sending emails: {request.recipient}")
    try:
        email_service = EmailService()
        result = email_service.send_email(request.template, request.recipient, request.images, request.custom_text)
        return {"message": "Emails sent", "results": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))