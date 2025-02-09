import time
class Llama:

    def __init__(self,name, gender, breed, age):
        self.name=name
        self.gender=gender
        self.breed=breed
        self.age=age
        self.hunger=25
        self.energy=100
        self.mentalhealth=25
        self.wool=25
    
    def show (self):
        print(f"Llama:{self.name} is a {self.gender} {self.breed}. {self.name} is {self.age} year(s) old ! ")
        print(f"Energy level is {self.energy}, and hunger level is {self.hunger}, and wool level is {self.wool}")

    def graze (self):
        self.hunger=self.hunger-5
        self.energy=self.energy+10
        self.mentalhealth=self.mentalhealth+10
        print(f"{self.name} just grazed some grass")
        
    def travel(self, kilometers, load):
        self.hunger=self.hunger+kilometers*load
        self.energy=self.energy-(kilometers*load*2)
        print(f"{self.name} just traveled for {kilometers} kilometers and carieed {load} tons")
        
    def sleep(self,hours):
        self.energy += (hours * 2)
        self.hunger += hours
        print(f"{self.name} just took a {hours}-minute sleep.")
        time.sleep(30)



    def hum(self):
        print(f"{self.name} says HMMMM")

    def emergency(self):
        print(f"{self.name} is in distress")

    def lick(self):
        print(f"{self.name} is hungry or thirsty")

    def happy(self):
        if self.mentalhealth>=40:
            print(f"{self.name} says mwa")
            print("           :*@@@@@@@@@@@#:           \n        .#@@@*-       -*@@@#.        \n       %@@+               +@@%       \n     -@@#                   #@@-     \n    :@@=                     -@@-    \n   .@@=     #@%       %@%     -@@.   \n   +@@     =#+##     ##+#=     @@+   \n   #@#                         #@#   \n   #@#      .           .      #@#   \n   +@@     @@@         @@@     @@+   \n   .@@=     %@@%:   :%@@%     -@@.   \n    :@@=      @@@@@@@@@      -@@-    \n     -@@#                   *@@-     \n       %@@+               +@@%.      \n        .%@@@*:       :+@@@%.        \n           :#@@@@@@@@@@@#-           ")
    
    def bonding(self):
        self.mentalhealth=self.mentalhealth+25
        print(f"{self.name} wants to spend time with you")
    def growing(self):
        self.age=self.age+1
        self.wool=self.wool+3
        self.hunger=self.hunger+2
        self.energy-=10


        






    