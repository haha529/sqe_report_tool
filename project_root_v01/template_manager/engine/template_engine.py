from jinja2 import Environment, FileSystemLoader


class TemplateEngine:
    def __init__(self, template_dir):
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def render(self, template_name, context):
        template = self.env.get_template(template_name)
        return template.render(context)

    def get_template_dir(self):
        return self.template_dir