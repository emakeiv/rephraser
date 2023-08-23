import openai


class OpenAiServiceClient:
    def __init__(self, key:str, model:str):
        openai.api_key = key
        self.model = model

    async def get_response(self, promt: str):
        try:
            messages = [{"role": "user", "content": promt}]

            response = openai.ChatCompletion.create(
                model=self.model, messages=messages, temperature=0
            )

            return [
                choice.get("message", {}).get("content", "")
                for choice in response["choices"]
            ]
        except Exception as e:
            print("Exception occurred:", e)
            raise
