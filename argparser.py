import argparse


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="terminal interface to Mistral Ai")
        self.parser.add_argument("key",type=str,help="Mistral AI API key.")
        self.parser.add_argument("-p","--prompt",type=str,default="",help="prompt to send.")
        self.parser.add_argument("-i","--interactive",action="store_true",help="run in interactive mode.")
        
        self.__args = self.parser.parse_args()

    def get_key(self):
        return self.__args.key

    def get_prompt(self):
        return self.__args.prompt

    def is_interactive(self):
        return self.__args.interactive

