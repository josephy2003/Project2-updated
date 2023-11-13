import random

import time

class Guitars:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def buildGuitar(self):

        #Guitar brand names
        self.brand = ['Fender', 'Gibson', 'Epiphone', 'Ibanez']

        fender_mod = ['Stratocaster', 'Telocaster', 'Jaguar', 'Mustang']
        gibson_mod = ['Les Paul', 'SG', 'XPlorer', 'FlyingV']
        epiphone = ['ES339', 'Crestwood', 'Willshire', '']
        ibanez = ['','','',]

        self.model = {'Fender': [fender_mod], 'Gibson': [gibson_mod], 'Epiphone': [epiphone]}




    def identifyGuitar(self):
        print("|𝙊𝙑𝙀𝙍𝙑𝙄𝙀𝙒|\n")
        time.sleep(.50)
        print("You guitar is a {}")


        wGuitar = input()
