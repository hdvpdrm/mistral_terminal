from mistralai import Mistral as Brain
import os

class Mistral:
    def __init__(self,key:str):
        os.environ["MISTRAL_API_KEY"] = key
        self.client = Brain(api_key=os.environ["MISTRAL_API_KEY"])
        self.model = "mistral-large-latest"
        
    def ask(self,prompt:str) -> str:
        '''send provided prompt to Mistral AI and returns its request'''
        chat_response = self.client.chat.complete(
            model= self.model,
            messages = [
                {
                    "role": "user",
                    "content": prompt,
                },
            ]
        )
        return chat_response.choices[0].message.content
