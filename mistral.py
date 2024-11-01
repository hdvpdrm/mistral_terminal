from mistralai import Mistral as Brain
import os

class Mistral:
    def __init__(self,key:str):
        os.environ["MISTRAL_API_KEY"] = key
        self.client = Brain(api_key=os.environ["MISTRAL_API_KEY"])
        self.model = "mistral-large-latest"
        
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
        print(chat_response.choices[0].message.content)

    def _ask_in_stream(self,prompt:str) -> None:
        res = self.client.chat.stream(model="mistral-small-latest", messages=[
            {
                "content": prompt,
                "role": "user",
            },
        ])
        length_counter = 0
        if res is not None:
            for event in res:
                # handle event
                data = event.data.choices[0]
                content = data.delta.content
                print(content,end="")
                length_counter+=len(content)
                if length_counter > 200:
                    print("")
                    length_counter = 0
        print("")

    def run(self,prompt:str,streaming:bool) -> None:
        if streaming:
            self._ask_in_stream(prompt)
        else:
            self._ask(prompt)
