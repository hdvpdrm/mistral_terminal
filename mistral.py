from mistralai import Mistral as Brain
from history import History
import os

class Mistral:
    def __init__(self,key:str):
        os.environ["MISTRAL_API_KEY"] = key
        self.client = Brain(api_key=os.environ["MISTRAL_API_KEY"])
        self.model = "mistral-large-latest"        
        self.history_manager = History()
        
    def _ask(self,prompt:str) -> None:
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
        response = chat_response.choices[0].message.content
        self.history_manager.add(prompt,response)
        print(response)

    def _ask_in_stream(self,prompt:str) -> None:
        res = self.client.chat.stream(model="mistral-small-latest", messages=[
            {
                "content": prompt,
                "role": "user",
            },
        ])
        length_counter = 0
        response = []
        if res is not None:
            for event in res:
                # handle event
                data = event.data.choices[0]
                content = data.delta.content
                response.append(content)
                print(content,end="")
                length_counter+=len(content)
                if length_counter > 200:
                    print("")
                    length_counter = 0
        print("")
        self.history_manager.add(prompt,"".join(response))

    def run(self,prompt:str,streaming:bool) -> None:
        if streaming:
            self._ask_in_stream(prompt)
        else:
            self._ask(prompt)
