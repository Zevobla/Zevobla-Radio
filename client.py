"""Client for controlling ZeRadio."""

import cmd

import requests

class CLI(cmd.Cmd):
    intro = "Welcome to my internet radio streaming app. Type help or ? to list commands.\n"
    prompt = "(Radio) $ "

    def do_add(self, arg):
        """Add smth to queue. add spotify:track:0UHB9METy4VCXNgkcGqHqS"""

        if "spotify" in arg:
            requests.post(f"http://radio.persifon.com:7002/track/{arg}", timeout=50)
            print("Added")
        else:
            print("Syntax: add spotify:track:0UHB9METy4VCXNgkcGqHqS")

    def do_start(self, arg):
        """Add smth to queue. add spotify:track:0UHB9METy4VCXNgkcGqHqS"""

        requests.get("http://radio.persifon.com:8082/start", timeout=50)
        print("STrated")
    
    def do_get_queue(self, arg):
        """Add smth to queue. add spotify:track:0UHB9METy4VCXNgkcGqHqS"""

        r = requests.get("http://radio.persifon.com:7002/current", timeout=50)
        print("STrated", r.text)

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
