import random, sys, time

from config import *

time.sleep(.50)

def return_Msg(m):
    print(f"\n'{m}'")

with open('fileoverview.txt', encoding='utf8') as f:
    final = f.read()
    print(final)


def main():
    choices = ['fender', 'gibson', 'epiphone', 'ibanez']
    time.sleep(1)
    myGuitar = input('Hello, what king of guitar are you looking for?: \n\n')

    myModel = input("")

    if myGuitar not in choices:
        print("Hmm, I don't know that one.")
        print(f"\n I know only, {[choices]}")
        exit()

    else:
        return_Msg(myGuitar)
        returnResponse()
        myGuitar += Guitars(brand=myGuitar, model=None, type=None)


















main()
