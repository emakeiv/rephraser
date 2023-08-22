import openai
from app.clients.templates.template_manager import template_manager
from app.clients.templates.template_preprocessor import template_preprocessor

class OpenAiServiceClient:
    def __init__(self, key):
        openai.api_key = key
        self.model = "gpt-3.5-turbo"
        self.template_manager = template_manager
        self.template_preprocessor = template_preprocessor
   
        
    async def get_response(self, user_input:dict, template_name:str):
      
        '''
        comes from process_phrase() in phrases.py
        {
            'text': 'Brown fox jumps over the lazy dog',
            'number_of_variants': 2
        }

        comes from generate_sections() in sections.py
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

        template = await self.template_manager.get_template(template_name)
        
        promt = self.template_preprocessor.preprocess_template(user_input, template)

        try:
            messages = [{"role": "user", "content": promt}]

            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=0
            )
            
            return [
                choice.get("message", {}).get("content", "")
                for choice in response["choices"]
            ]
        except Exception as e:
            print("Exception occurred:", e)
            raise