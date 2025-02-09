# Creating a Cat class
# Use a “Cat” class to represent an individual cat.
# The initializer method must initialize instance variables for name, gender, breed, age, hunger, and energy levels.
# The initial value for hunger is 50. The initial value for energy is also 50.
# The initial values for name, gender, breed, and age must be passed as arguments to the initializer.

# Adding methods
# Ensure all functionality from the procedural code is preserved in the object-oriented version.

class Cat:

    def __init__(self,name, gender, breed, age):
        self.name=name
        self.gender=gender
        self.breed=breed
        self.age=age
        self.hunger=50
        self.energy=50

    
    def show (self):
        print(f"Cat:{self.name} is a {self.gender} {self.breed}. {self.name} is {self.age} year(s) old ! ")
        print(f"Energy level is {self.energy}, and hunger level is {self.hunger}")

    def eat (self):
        self.hunger=self.hunger-5
        self.energy=self.energy+10
        print(f"{self.name} just ate some food")
        
    def play(self, minutes):
        
        self.hunger=self.hunger+minutes
        self.energy=self.energy-(minutes*2)
        print(f"{self.name} just played for {minutes} minutes")
        
    def nap(self,hours):
        self.energy += (hours * 5)
        self.hunger += hours
        print(f"{self.name} just took a {hours} hour nap.")

    def meow(self):
        self.energy = self.energy - 2
        print(f"{self.name} says MEOW")


    
# make an object of Cat class. Then ask user to press S to show details, E to make it eat, P to play, S to make it sleep, M to make it speak.
# make a method called add_pet , display_pet , display_app_pets
class Petshelter:

    def __init__(self):
        self.petsDict = {}
        self.petsid = -1
    
    def add_pet(self, pet_name:str , pet_gender : str, pet_breed : str, pet_age :int ):
        newpet = Cat(pet_name, pet_gender, pet_breed, pet_age)
        self.petsid = self.petsid+1
        self.petsDict[self.petsId]= newpet
        return self.petsId
    
    def display_pet(self,selfid):
        pass
        



    


pet_Shelter= Petshelter()
        