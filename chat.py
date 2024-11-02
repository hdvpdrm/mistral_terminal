from mistral import Mistral
from colors import color
import os
import time
import signal
import readline

def catch_interruption_c(signal, frame):
    print("\n work is done. Hope it was helpful!")
    exit(0)

class Chat:
    def __init__(self,key:str,streaming:bool):
        self.m = Mistral(key)
        self.stream = streaming
    
    def __is_input_ok(self,s):
        check = False
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                check = True
        return check

    def __run_chat(self):
        print(color.blue+"[you]:"+color.end,end="")

        s = "".join(list(iter(input, '')))
        print(color.warning+"[system message]:"+color.end,end="")
        print("please, stand by")
        if self.__is_input_ok(s):           
            print(color.yellow+"[robot]:"+color.end+"\n")
            self.m.run(s,self.stream)

            
    def run(self):
        signal.signal(signal.SIGINT, catch_interruption_c)      
        os.system("clear||cls")
        while True:
            self.__run_chat()
            
        signal.pause()
