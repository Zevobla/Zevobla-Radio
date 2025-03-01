import uvicorn
from fastapi import FastAPI

import requests

import cmd

class CLI(cmd.Cmd):
    intro = "Welcome to my internet radio streaming app. Type help or ? to list commands.\n"
    prompt = "(Radio) $ "

    def do_add(self, arg):
        """Add smth to queue. add spotify:track:0UHB9METy4VCXNgkcGqHqS"""

        if "spotify" in arg:
            requests.post(f"127.0.0.1:8081/{arg}", timeout=50)
            print("Added")
            return True
        else:
            print("Syntax: add spotify:track:0UHB9METy4VCXNgkcGqHqS")

    def do_login(self, arg):
        """Do login to the radio server"""


    def do_exit(self, arg):
        """Exit the shell: exit"""

        print("Exiting...")

        return True

    def do_EOF(self, arg):
        """Exit the shell with Ctrl+D:"""

        print("Exiting...")

        return True

if __name__ == "__main__":
    CLI().cmdloop()
