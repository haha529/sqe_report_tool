import os

from template_manager.engine.template_engine import TemplateEngine
from template_manager.context.template_context import TemplateContextManager
from template_processor import TemplateProcessor


class ReportTemplateProcessor(TemplateProcessor):
    def __init__(self, engine: TemplateEngine, context_manager: TemplateContextManager):
        super().__init__(engine, context_manager)
        self.template_name = "report_template"

    def extract_group_variables(self, group_name):
        context = self.context_manager.load_context()
        return context.get(group_name, {})

    def extract_urls_from_context(self):
        context = self.context_manager.load_context()
        summary_urls = context.get('summary', {}).get('urls', [])
        detail_urls = context.get('detail', {}).get('urls', [])
        return summary_urls, detail_urls
