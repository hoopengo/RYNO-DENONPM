from sys import argv
from os import path, remove, system
from colorama import Fore
from json import *

try:
    # print(argv[1]) # DEBUG mode
    if argv[1] == 'init' and not path.isfile('package.json') or argv[1] == 'i' and not path.isfile('package.json'):
        name = input('Name(DENO): ')
        name = 'DENO' if name == '' else name
        version = input('Version(0.0.0): ')
        version = '0.0.0' if version == '' else version
        author = input('Author(Ryno): ')
        author = 'Ryno' if author == '' else author
        with open('package.json', 'w', encoding='utf-8') as f:
            f.write("{\n")
            f.write(f'\t"name": "{name}",\n')
            f.write(f'\t"version": "{version}",\n')
            f.write(f'\t"author": "{author}",\n')
            f.write('\t"scripts": {\n')
            f.write('\t\t"start": "deno run --allow-net index.ts"\n')
            f.write("\t}\n")
            f.write("}")
            print(f"file '{Fore.GREEN}package.json{Fore.WHITE}' will be created!")
    elif argv[1] == 'run' and path.isfile('package.json'):
        ff = open('package.json', 'r', encoding='utf-8')
        ff = loads(ff.read())
        try:
            print(f'{Fore.RED}[RYNO] {Fore.YELLOW}You are starting {Fore.GREEN}{argv[2]}{Fore.YELLOW} command{Fore.WHITE}')
            item = ff["scripts"][argv[2]]
            system(item)
        except Exception as error:
            print(error)
            try:
                itm = ''
                for item in ff["scripts"]:
                    itm += f"{item} \n"
                print(f'Running is empty! Your commands: {itm}')
            except Exception as e:
                print(e)
    else:
        if path.isfile('package.json'):
            print('OK! This file already been created..')
            if input("Delete this file?(Y/n): ").lower() == 'y':
                remove('package.json')
                print(f"file has been removed: {Fore.RED}ryno init{Fore.WHITE}")
        elif not path.isfile('package.json'):
            print(f"Please make the '{Fore.GREEN}package.json{Fore.WHITE}' file: {Fore.RED}ryno init{Fore.WHITE}")
        else:
            print(f"What's going on? I dont forget this command!) - {argv[1]}")
except:
    print("You don't indicate command")

#  DEBUG mode

# print(ff["scripts"])
# for item in ff["scripts"]["start"]:
#     print(item)