#!/usr/bin/env python

import signal
import sys, os
import json
from collections import OrderedDict 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class commands:
    dev = ""
    demo = ""
    fastgoed = ""

def signal_handler(signal, frame):
  print("\r")
  sys.exit(0)

def get_menu_choice():
    def print_menu():
        title = (30 * '-') + " [ Build Environment ] " + (30 * '-')
        print(bcolors.HEADER + title + bcolors.ENDC)
        print("\r")
        print(bcolors.OKBLUE + "\t 1. (Default) -- Request certificate" + bcolors.ENDC)
        # print(bcolors.OKBLUE + "\t 2. temp menu item " + bcolors.ENDC)
        print(bcolors.FAIL + "\t 0. [Exit] " + bcolors.ENDC)
        print("\r")
        print(bcolors.HEADER + (83 * "-") + bcolors.ENDC)

    loop = True

    while loop:
        print_menu()
        choice = input("Enter your choice [0-3]: ")
        choice = int(choice)

        if choice == 1:
            command = 'default'
            loop = False
        # elif choice == 2:
        #     command = 'createcss'
        #     loop = False
        elif choice == 0:
            loop = False
            print("\r")
            sys.exit(0)
        else:
            input(bcolors.FAIL + "Wrong menu selection. Enter any key to try again.." + bcolors.ENDC)
    return command

header = '''\

--------------------------------------------------------------------
   Wildcard cert generator
--------------------------------------------------------------------
                                           
                                           (c) 2020, DevSchuur.io
'''

print(bcolors.OKGREEN + header + bcolors.ENDC)

signal.signal(signal.SIGINT, signal_handler)
command = get_menu_choice()

print("\r\r")
print(bcolors.HEADER + (83 * "-") + bcolors.ENDC)
print(bcolors.OKBLUE + "\r *** Building environment with command: " + str(command) + " ***" + bcolors.ENDC + "\r")
print(bcolors.HEADER + (83 * "-") + bcolors.ENDC + "\r")

default_commands = OrderedDict()

default_commands['Removing old data docker volumes'] = "docker-compose down -v --remove-orphans"
default_commands['Building new dockerimages, if needed'] = "docker-compose build"
default_commands['Starting environment'] = "docker-compose up -d"
default_commands['Execute step - Request Certificate'] = "docker-compose exec app /usr/bin/python3 cert.py"


for desc, command in default_commands.items():
    print(bcolors.OKBLUE + "-- " + desc + "..."+ bcolors.ENDC)
    try:
        print("executing command: " + command)
        os.system(command)
    except:
        print(bcolors.FAIL + "Whoops, something went wrong..." + bcolors.ENDC)
