import os

class TemplateManager:
    def __init__(self):
        self.templates = {}

    async def load_templates(self):
        module_path = os.path.dirname(os.path.abspath(__file__))
        template_files = [filename for filename in os.listdir(module_path) if filename.endswith(".txt")]

        for filename in template_files:
            with open(os.path.join(module_path, filename), "r") as f:
                template_name = os.path.splitext(filename)[0] 
                self.templates[template_name] = f.read()

    async def get_template(self, template_name: str):
        await self.load_templates()
        try:
            return self.templates.get(template_name, None)
        except FileNotFoundError:
            raise
            
template_manager = TemplateManager()
template_manager.load_templates()
