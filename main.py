import argparse
from platform import python_version
from commands import ping
import os
import getpass
import platform

parser = argparse.ArgumentParser(description='A command line shell built for simplicity on a high level programming language')
parser.add_argument('-v','--verbose', help='Enable debug mode(developer)', action='store_true')
args = parser.parse_args()
v = args.verbose
platform = platform.system()
username = getpass.getuser()
if platform == "Windows":
    os.system("@echo off")
    os.system("color")

# note to self: print("\033[1;32;40m Bright Green  \n")
#           ANSI escape: https://ozzmaker.com/add-colour-to-text-in-python/            
 
if v == True:
    print("\033[0;37;42m You are running python-command-line in debug mode. \033[0m")
    print("\033[0;32;40m version 0.0.1 alpha \033[0m")
print("Running on python " + python_version());
print("\033[1;32;40mwelcome to PYSH \033[0m")


command = input(f"{username}: PYSH >> ")

for file in os.listdir(f"{os.getcwd()}/commands"):
    if file.endswith(".py"):
        if file.find(command) != -1:
            command += ".main()"
            exec(command)
            if getattr(command.value, "end_code") == 0:
                if v == True:
                    print("\033[0;37;42m successfully ran command:  \033[0m")
                exit(0)
            else:
                print("\033[0;37;41m command was not completed correctly, killing program \033[0m")
        else:
            print("\033[0;37;41m command was not found, killing program \033[0m")
            exit(-1)


