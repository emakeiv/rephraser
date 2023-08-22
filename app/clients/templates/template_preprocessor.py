from app.common.utilities import flatten_dict

class TemplatePreprocessor:

    def preprocess_template(self, user_input: dict, template: str) -> str:

        '''
        {
            'text': 'Brown fox jumps over the lazy dog',
            'number_of_variants': 2
        }

        {
            'description': 'Company sales quality cofins because death is always in demand', 
            'sections': {
                    'about': {
                        'title': 1, 
                        'subtitle': None, 
                        'description': 2
                    }
            }
        }
        '''

        dynamic_sections = ""
        for section_name, section_data in user_input.get("sections", {}).items():
            dynamic_sections += f"\n-- {section_name} --\n"
            for field_name, field_value in section_data.items():
          
                if field_value is not None:
                    dynamic_sections += f"{field_name.capitalize()}: {field_value}\n"
                   
        user_input["dynamic_sections"] = dynamic_sections
        #print(user_input)
        return template.format(**flatten_dict(user_input))
       
 


template_preprocessor = TemplatePreprocessor()