import os

class TemplateManager:

    async def load_templates(self):
        module_path = os.path.dirname(os.path.abspath(__file__))
        template_files = [
            filename
            for filename in os.listdir(module_path)
            if filename.endswith(".txt")
        ]

        templates = {}
        for filename in template_files:
            with open(os.path.join(module_path, filename), "r") as f:
                template_name = os.path.splitext(filename)[0]
                templates[template_name] = f.read()

        return templates

    async def get_template(self, template_name: str):
        templates = await self.load_templates()
        try:
            return templates.get(template_name, None)
        except FileNotFoundError:
            raise

