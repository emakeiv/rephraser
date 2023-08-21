import openai


class OpenAiServiceClient:
    def __init__(self, key):
        openai.api_key = key
        self.model = "gpt-3.5-turbo"
        self.activated = True

    def get_heartbeat(self):
        return True

    def preprocess(self, entry: str):
        prompt = f"""
       Your task is to generate rephrased text based on a user given text.
       Make sure the rehprased text composition is completelty different from original
       Consider this user input example:
       - The first pair of Shleps was knit by Edu's grandma - as a gift for a climbing grandson. Wasn't long
       before people in the climbing gym started noticed and putting ideas into our heads - so here we are!
       Desirable transformation example:
       - Edu's grandma lovingly knitted the intial set of Shleps as a special present for her adventurous grandson
       who enjoyed climbing. It didn't take much time for others at the climbing gym to take notice and inspire us
       with their suggestions, leading us to where we are today!
       
       Text sample: '''{entry}'''
       """
        return prompt

    def get_response(self, user_input: str, variants: int):
        messages = [{"role": "user", "content": self.preprocess(user_input)}]
        if self.activated:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=1,
                n=variants,
                frequency_penalty=1,
                presence_penalty=1,
            )
        return [
            choice.get("message", {}).get("content", "")
            for choice in response["choices"]
        ]
