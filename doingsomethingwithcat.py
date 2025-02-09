from cat import Cat

pawsjunior = Cat("pawsjunior","male","balinese",0.7)

while True:
    thing_to_do=input("\nWhat do you want to make your cat to do?\n Press D to show details, E to make it eat, P to play, S to make it sleep, M to make it speak. Press Q to exit ! ")
    if len(thing_to_do) >1: #checking if input is longer than 1 letter
        thing_to_do=thing_to_do[0]
    thing_to_do= thing_to_do.upper()
    
    if thing_to_do=="D":
        pawsjunior.show()
    
    elif thing_to_do=="E":
        pawsjunior.eat()
    
    elif thing_to_do=="P":
        min = int(input("how many minutes has the cat played? "))
        pawsjunior.play(min)
    
    elif thing_to_do=="M":
        pawsjunior.meow()
    
    elif thing_to_do=="S":
        sleep = int(input("how many minutes has the cat sleep"))
        pawsjunior.nap(sleep)
    
    elif thing_to_do=="Q":
        break
    
print("Bye!")
    
    
   

    
    
