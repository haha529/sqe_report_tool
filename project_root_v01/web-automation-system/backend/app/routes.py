import json
import os
import logging

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.config import get_templates_dir
from app.models import ScreenshotRequest, EmailRequest, TemplateRequest
from app.services.screenshot_service import ScreenshotService
from app.services.email_service import EmailService
from app.utils.logging_config import setup_logging
from jinja2 import Environment, FileSystemLoader, meta

setup_logging()
router = APIRouter()

@router.get("/templates")
def get_templates():
    try:
        templates = [f.replace(".html", "") for f in os.listdir(get_templates_dir()) if f.endswith('.html')]
        return {"templates": templates}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/template/{template_name}")
def get_template(template_name: str):
    try:
        with open(os.path.join(get_templates_dir(), template_name + ".html"), 'r') as file:
            content = file.read()
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/template/{template_name}")
def save_template(template_name: str, request: TemplateRequest):
    try:
        with open(os.path.join(get_templates_dir(), template_name + ".html"), 'w') as file:
            file.write(request.content)
        return {"message": "Template saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/template/{template_name}/context")
def get_template_context(template_name: str):
    try:
        json_filename = template_name + ".json"
        if not os.path.exists(os.path.join(get_templates_dir(), json_filename)):
            logging.error(f"Context file not found: {json_filename}")
            return {"context": {}}
        with open(os.path.join(get_templates_dir(), json_filename), 'r') as file:
            template_json = json.loads(file.read())
        return {"context": template_json}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/template/{template_name}/context")
def save_template_context(template_name: str, request: dict):
    try:
        json_filename = template_name + ".json"
        with open(os.path.join(get_templates_dir(), json_filename), 'w') as file:
            file.write(json.dumps(request, indent=4))
        return {"message": "Context saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/template/{template_name}/render")
def render_template(template_name: str):
    try:
        json_filename = template_name + ".json"
        html_filename = template_name + ".html"

        with open(os.path.join(get_templates_dir(), json_filename), 'r') as file:
            template_context = json.load(file)

        env = Environment(loader=FileSystemLoader(get_templates_dir()))
        template = env.get_template(html_filename)
        content = template.render(template_context)

        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/template/{template_name}/index.html")
def render_template_index(template_name: str):
    try:
        result = render_template(template_name)
        return JSONResponse(content=result["content"], media_type="text/html")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/template/{template_name}/screenshots")
def template_screenshots(template_name: str):
    try:
        json_filename = template_name + ".json"
        with open(os.path.join(get_templates_dir(), json_filename), 'r') as file:
            template_json = json.loads(file.read())

        screenshot_service = ScreenshotService()
        results = []
        for item in template_json:
            if isinstance(template_json[item], list):
                logging.info(f"Taking screenshots for: list {item}")
                for e in template_json[item]:
                    if e["screenshot"] == "True":
                        logging.info(f"Taking screenshot: {e['name']}")
                        result = screenshot_service.capture_screenshot(e["name"], e["url"], e["width"], e["height"])
                        results.append(result)
        return {"message": "Screenshots taken", "screenshots": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/send-email")
def send_email(request: EmailRequest):
    logging.info(f"Sending emails: {request.recipient}")
    try:
        email_service = EmailService()
        result = email_service.send_email(request.template, request.recipient, request.images, request.custom_text)
        return {"message": "Emails sent", "results": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))