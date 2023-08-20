
import openai

class OpenAiServiceClient:
    def __init__(self, model: str, top_p: int, n: int):
        self.model = model
        self.top_p = top_p
        self.choices = n

    def get_response(self, input:str, n:int):
        messages = [{
            "role": "user", 
            "content": input
        }]
        return 
        {
            "choices": [
                {
                "finish_reason": "stop",
                "index": 0,
                "message": {
                    "content": "The sentiment of the product review is positive.",
                    "role": "assistant"
                }
                },
                {
                "finish_reason": "stop",
                "index": 1,
                "message": {
                    "content": "The sentiment of the product review is positive.",
                    "role": "assistant"
                }
                }
            ],
            "created": 1692549496,
            "id": "chatcmpl-7pfjMLZi36auPt60CULx3aQM0nUAO",
            "model": "gpt-3.5-turbo-0613",
            "object": "chat.completion",
            "usage": {
                "completion_tokens": 18,
                "prompt_tokens": 134,
                "total_tokens": 152
            }
        }
        # response = openai.ChatCompletion.create(
        #     model=self.model,
        #     messages = messages,
        #     top_p= self.top_p,
        #     n = self.choices
        # )