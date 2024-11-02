import json
import os
from datetime import datetime

class History:
    def __init__(self):
        self.path = os.path.expanduser("~")+"/.mistral_chat_history"
        self.data = self._read_history()
    def _read_history(self) -> dict:
        if not os.path.exists(self.path): return {}

        try:
            with open(self.path,"r") as f:
                return dict(json.loads(f.read()))            
        except Exception as e:
            print(str(e))
            return {}
        
    def _dump_history(self) -> None:
        try:
            with open(self.path,"w") as f:
                f.write(json.dumps(self.data))
        except Exception as e:
            print(str(e))            

    def __del__(self):
        self._dump_history()

    def _get_curr_date(self) -> str:
        current_time = datetime.now()
        return current_time.strftime("%Y-%m-%d%H:%M:%S")
    
    def add(self,request:str,response:str) -> None:
        self.data[self._get_curr_date()] = (request,response)

    
