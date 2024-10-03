from pydantic import BaseModel
from typing import List


class ScreenshotParams(BaseModel):
    url: str
    width: int
    height: int

class ScreenshotRequest(BaseModel):
    screenshots: List[ScreenshotParams]


class EmailParams(BaseModel):
    template: str
    recipient: str
    images: List[str]
    custom_text: str

class EmailRequest(BaseModel):
    email: List[EmailParams]


class Email:
    def __init__(self, recipient, subject, body):
        self.recipient = recipient
        self.subject = subject
        self.body = body

class Screenshot:
    def __init__(self, id, url=None, image_path=None):
        self.id = id
        self.image_path = image_path
        self.url = url


class TemplateRequest(BaseModel):
    content: str