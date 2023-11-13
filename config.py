import time, random


gtr = """                      ▒▒▒▒              
                    ▓▓▒▒▒▒░░            
                  ▓▓▒▒▒▒▒▒              
                  ██▒▒▒▒░░              
                  ▓▓▒▒▒▒░░              
                ▒▒▒▒▒▒▒▒▒▒              
                ██▒▒▒▒▒▒▒▒              
                ██▒▒▒▒▒▒▒▒              
                ██▒▒▒▒▒▒▒▒              
                ░░▒▒▒▒▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒██▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒██▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒██▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒██▒▒                
                  ▒▒▒▒▒▒                
                  ▒▒▒▒▒▒                
                  ▓▓▒▒▓▓                
      ░░          ▒▒██▒▒                
    ▓▓▓▓▓▓        ▒▒▒▒▒▒                
    ▓▓▓▓▓▓        ▒▒██▒▒                
    ▓▓▓▓▓▓▓▓      ▒▒▒▒▒▒          ▓▓    
      ▓▓▓▓▓▓▓▓▓▓▒▒▒▒██▒▒        ▓▓░░▒▒  
      ▓▓▓▓▓▓▓▓▓▓░░▒▒▒▒▒▒▓▓      ▓▓░░▓▓  
        ▓▓▓▓▓▓▓▓░░▒▒██▒▒▒▒░░▒▒░░▒▒░░▓▓  
        ▓▓▓▓▓▓▓▓░░▒▒▒▒▒▒░░░░░░░░░░░░▓▓  
        ▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓    
        ▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓    
        ▓▓▓▓▓▓▓▓░░▒▒▒▒▒▒░░░░░░░░▓▓      
        ▓▓▓▓▓▓▒▒░░      ░░░░░░░░▒▒▒▒    
        ▓▓▓▓▓▓░░░░▒▒▒▒▒▒░░░░░░░░░░▓▓    
      ▓▓▓▓▓▓▓▓░░░░▒▒▒▒▒▒░░░░░░░░░░░░▓▓  
      ▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓  
    ▒▒▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓
  ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▓▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░▓▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
"""


def returnResponse():
    ai_response = ['Cool! I like their guitars ;)', 'Good tasteee!', 'OK!']

    randomize = random.choice(ai_response)

    print(randomize)


class Guitars:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def buildGuitar(self):

        #Guitar type
        fender_mod = ['Stratocaster', 'Telecaster', 'Jazzmaster', 'Mustang']
        gibson_mod = ['Les Paul', 'SG', 'Explorer', 'Flying V']
        epiphone_mod = ['ES339', 'Crestwood', 'Wilshire']
        ibanez_mod = ['RG', 'GRX', 'Genesis']

        self.models = {'fender': fender_mod, 'gibson': gibson_mod, 'epiphone': epiphone_mod, 'ibanez': ibanez_mod}

        self.type = ['Electric', 'Acoutsic']

    def identifyGuitar(self):
        print("|𝙊𝙑𝙀𝙍𝙑𝙄𝙀𝙒|\n")
        time.sleep(.50)
        print(f"You guitar is a {self.brand}. It's the, {self.model}. It's an {self.type}. \n")
        time.sleep(.50)
        print(gtr)



