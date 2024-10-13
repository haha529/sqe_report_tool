from template_manager.context.template_context import TemplateContextManager
from template_manager.engine.template_engine import TemplateEngine
from template_processor import TemplateProcessor


class EmailTemplateProcessor(TemplateProcessor):
    def __init__(self, engine: TemplateEngine, context_manager: TemplateContextManager):
        super().__init__(engine, context_manager)
        self.template_name = "email_template"

    def extract_group_variables(self, group_name):
        return {}

    def extract_urls_from_context(self):
        return [], []