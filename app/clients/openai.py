import openai

class OpenAiServiceClient:
    def __init__(self, key:str, model: str, top_p: int, n: int):
        self.key = key
        self.model = model
        self.top_p = top_p
        self.choices = n

    def get_response(self, input:str):
        # messages = [{
        #     "role": "user", 
        #     "content": input
        # }]
        
        # response = openai.ChatCompletion.create(
        #     model=self.model,
        #     messages = messages,
        #     top_p= self.top_p,
        #     n = self.choices
        # )

        return ["Hello", "Service"]