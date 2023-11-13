import random
import sys
import time


time.sleep(.50)

def return_Msg(m):
    print(f"\n'{m}'")

with open('fileoverview.txt', encoding='utf8') as f:
    final = f.read()
    print(final)


def main():
    choices = ['Fender', 'Gibson', 'Epiphone', 'Schecter']
    time.sleep(1)
    user_input = input('Hello, what king of guitar are you looking for?: \n\n')
    return_Msg(user_input)

    if user_input == [choices]:
        user_input

    elif user_input != "":
        exit()












main()
