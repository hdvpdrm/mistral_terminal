#!/usr/bin/python3
import sys
try:
    from mistral import Mistral
    from argparser import Parser
except Exception as e:
    print(str(e))
    sys.exit(-1)


if __name__ == "__main__":
    parser = Parser()
    m = Mistral(parser.get_key())
    if not parser.is_interactive():
        if parser.get_prompt() == "":
            print("error: no prompt to send!")
            sys.exit(-2)

        print(m.ask(parser.get_prompt()))
        
