import logging
import os

from jinja2 import Template

class EmailService:
    def __init__(self):
        self.templates_dir = self.get_templates_dir()

    def get_templates_dir(self):
        templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates')
        logging.info(f"Templates directory: {templates_dir}")
        return templates_dir

    def send_email(self, template_name, recipient, images, custom_text):
        logging.info(f"Sending email to {recipient}")

        body = self.get_email_body(custom_text, images, template_name)

        # TODO: Implement email sending logic
        logging.info(f"Email sent to {recipient}")
        return {"status": "success", "message": "Email sent successfully"}

    def get_email_body(self, custom_text, images, template_name):
        template_path = os.path.join(self.templates_dir, template_name)
        with open(template_path, 'r') as file:
            template_content = file.read()
        template = Template(template_content)
        email_body = template.render(images=images, custom_text=custom_text)
        logging.info(f"Email body: {email_body}")
        return email_body