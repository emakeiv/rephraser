import os
from app.common.utilities import flatten_dict


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
            with open(os.path.join(module_path, filename), "r", encoding="utf-8") as f:
                template_name = os.path.splitext(filename)[0]
                templates[template_name] = f.read()

        return templates
    
    def preprocess_template(self, template: str, user_input: dict) -> str:
        dynamic_sections = ""
        for section_name, section_data in user_input.get("sections", {}).items():
            dynamic_sections += f"\n-- {section_name} --\n"
            for field_name, field_value in section_data.items():
                if field_value is not None:
                    dynamic_sections += f"{field_name.capitalize()}: {field_value}\n"

        user_input["dynamic_sections"] = dynamic_sections
        return template.format(**flatten_dict(user_input))

    async def form_template(self, user_input: dict, template_name: str):
       
        templates = await self.load_templates()
        template = templates.get(template_name)

        preprocessed = self.preprocess_template(template, user_input)
        if template is None:
            raise FileNotFoundError(f"Template '{template_name}' was not found.")
        return preprocessed
    

