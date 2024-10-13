import json
import os


class TemplateContextManager:
    def __init__(self, template_dir, template_name, version):
        self.context_file = f"{template_dir}/{template_name}/context_{version}.json"
        self.template_file = f"{template_name}/{template_name}.html"

    def load_context(self):
        with open(self.context_file, 'r') as f:
            return json.load(f)

    def save_context(self, context):
        with open(self.context_file, 'w') as f:
            json.dump(context, f, indent=4)

    def delete_context(self):
        if os.path.exists(self.context_file):
            os.remove(self.context_file)

    def update_context_variable(self, key, value):
        context = self.load_context()
        context[key] = value
        self.save_context(context)

    def get_template_file(self):
        return self.template_file