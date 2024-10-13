from abc import ABC, abstractmethod

from template_manager.context.template_context import TemplateContextManager
from template_manager.engine.template_engine import TemplateEngine


class TemplateProcessor(ABC):
    def __init__(self, engine: TemplateEngine, context_manager: TemplateContextManager):
        self.engine = engine
        self.context_manager = context_manager
        self.template_name = None

    def render_template(self, context):
        return self.engine.render(self.context_manager.get_template_file(), context)

    @abstractmethod
    def extract_group_variables(self, group_name):
        pass

    @abstractmethod
    def extract_urls_from_context(self):
        pass

    def load_context(self):
        return self.context_manager.load_context()

    def save_context(self, context):
        self.context_manager.save_context(context)

    def update_context_variable(self, key, value):
        self.context_manager.update_context_variable(key, value)