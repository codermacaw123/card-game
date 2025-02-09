from llama import Llama
import time
import random
import threading

sleepusmaxiums=Llama("sleepusmaxiums","male","sleepyandfluffy",3)
inputs=""
events = ""
print("_     _                             _                 _       _             \n| |   | |                           (_)               | |     | |            \n| |   | | __ _ _ __ ___   __ _   ___ _ _ __ ___  _   _| | __ _| |_ ___  _ __\n| |   | |/ _` | '_ ` _ \ / _` | / __| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|\n| |___| | (_| | | | | | | (_| | \__ \ | | | | | | |_| | | (_| | || (_) | |   \n\_____/_|\__,_|_| |_| |_|\__,_| |___/_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   ")
print("                                                      --::       \n                                                    --=++-....     \n                                                 -::-++-:......   \n                                                 -:.::=:=--:::..:  \n                                                -::..-::.-++:....  \n                                                -::..-::.-++:....  \n                                               --:.....:::.      .:\n                                               --:...:-::.:    . ..\n                                               -:.....--::::...:++ \n                                               -:.....-=--:--=     \n                                               -.......:-==+*      \n                                               -:......::-=+*      \n            ----:-----==                       -........::-=+      \n       ----::::...::...:::-:-----===  =       =:.........:-=       \n     --::.......................::::-:::::-::--..... ...:::=       \n  +=-:..............................:.............    ..:::=*    \n =-:.:.........................................      ...::-=    \n=+-::-:.....................   .       .        ... ....:-=+       \n=-::-.....  ...............                    .........:=+        \n=-:-:...... ................              .    ........:-=+        \n+=--=:...........:=...........          ............::-=++         \n +===-...........:=::..............................:::-+           \n   +==-:..........-=:::.........................:::::-++           \n      =-:..........-+=-:::.:..................:::::-+*             \n       -::.......:-=+ +=--::::....::::........::::=++              \n       -::::..:::-==     +====----==-::.::::::-==+++               \n      =-:::....:-=                 ++-::::::===--=+                \n     =--::::..:-++                  +-::....=----+                 \n     =-::::::-=+                    +=-:....-=::=                  \n     =--:::=+-::                    ==::....-:.:                   \n       ---=:.-..:                    =-::..:-:==                   \n        ---. ::.:-                   +=-::-=-:::                   \n          =:..:===                    +=++:-:.:                    \n           =---                        -:..-:.::                   \n")
def evens():
    while True:
        events = random.randint(1,25)

def everything():
    while True:
        
        inputs = input("press B to bond, press G to make your llama graze grass press Q to quit the application: ")
        if inputs == "B" or inputs == "G" or inputs == "S" or inputs == "":
            time.sleep(2)
            print(f"Your llama's mental health is {sleepusmaxiums.mentalhealth} and he has {sleepusmaxiums.hunger} hunger.")
            print(f"{sleepusmaxiums.name} is now {sleepusmaxiums.age} years old, and he has {sleepusmaxiums.wool} kg of wool.")
            choice = random.randint(1,4)
          
            print("choice",choice)
                
            if events==25:
                print("Your llama died of disease")

            if choice == 1:
                inputs = input("press B to bond, press G to make your llama graze grass press Q to quit the application: ")
            elif choice == 2:
                sleepusmaxiums.lick()
                inputs = input("press B to bond, press G to make your llama graze grass press Q to quit the application: ")
            elif choice == 3:
                if sleepusmaxiums.mentalhealth >=25:
                    sleepusmaxiums.happy()
                else:
                    sleepusmaxiums.bonding()
                    inputs = input("press B to bond, press G graze grass to make your llama press Q to quit the application: ")
            elif choice ==4:
                sleepusmaxiums.hum()
                
            if inputs == "B":
                sleepusmaxiums.bonding()
            if inputs == "G":
                sleepusmaxiums.graze()
            if inputs == "S":
                sleepusmaxiums.wool=sleepusmaxiums.wool-25
            
            if sleepusmaxiums.age >=10:
                "Your llama died, and he lived a very happy life!"
                break
            if sleepusmaxiums.mentalhealth <= 0:
                print('your llama ran away, you should have treated him better.')
            if sleepusmaxiums.wool >=30:
                print("please shave your llama")
                inputs = input("press B to bond, press G to make your llama graze, press S to shave your llama, press T to travel,  press Q to quit the application: ")

            if sleepusmaxiums.wool >=45:
                    print("Shave your llama or else he may pass away")
                    inputs = input("press B to bond, press G to make your llama graze, press S to shave your llama, press T to travel,  press Q to quit the application: ")

            if sleepusmaxiums.wool >=60:
                    print("Your llama died.")
                    break
            if sleepusmaxiums.hunger >=25:
                print("Your llama is very hungry")
                inputs = input("press B to bond, press G to make your llama graze, press S to shave your llama, press T to travel,  press Q to quit the application: ")
            if sleepusmaxiums.hunger>= 40:
                print("Your llama dies of starvation.")
            if sleepusmaxiums.energy<=0:
                sleepusmaxiums.sleep()
            if sleepusmaxiums.wool<=0:
           
                break

def growing():
    while True:
        
        time.sleep(20)
        sleepusmaxiums.growing()
        print(f"Your llama's mental health is {sleepusmaxiums.mentalhealth} and he has {sleepusmaxiums.hunger} hunger.")
        print(f"{sleepusmaxiums.name} is now {sleepusmaxiums.age} years old, and he has {sleepusmaxiums.wool} kg of wool.")
      
        if sleepusmaxiums.age>=10:
            print('         _______           _______    _        _        _______  _______  _______    ______  _________ _______  ______                _ \n|\     /|(  ___  )|\     /|(  ____ )  ( \      ( \      (  ___  )(       )(  ___  )  (  __  \ \__   __/(  ____ \(  __  \              / )\n( \   / )| (   ) || )   ( || (    )|  | (      | (      | (   ) || () () || (   ) |  | (  \  )   ) (   | (    \/| (  \  )   _        / / \n \ (_) / | |   | || |   | || (____)|  | |      | |      | (___) || || || || (___) |  | |   ) |   | |   | (__    | |   ) |  (_)_____ ( (  \n  \   /  | |   | || |   | ||     __)  | |      | |      |  ___  || |(_)| ||  ___  |  | |   | |   | |   |  __)   | |   | |    (_____)| |  \n   ) (   | |   | || |   | || (\ (     | |      | |      | (   ) || |   | || (   ) |  | |   ) |   | |   | (      | |   ) |   _       ( (  \n   | |   | (___) || (___) || ) \ \__  | (____/\| (____/\| )   ( || )   ( || )   ( |  | (__/  )___) (___| (____/\| (__/  )  (_)       \ \ \n   \_/   (_______)(_______)|/   \__/  (_______/(_______/|/     \||/     \||/     \|  (______/ \_______/(_______/(______/              \_)')
            break

        if sleepusmaxiums.wool>=60:
            print("Your llama died.")
            print('         _______           _______    _        _        _______  _______  _______    ______  _________ _______  ______                _ \n|\     /|(  ___  )|\     /|(  ____ )  ( \      ( \      (  ___  )(       )(  ___  )  (  __  \ \__   __/(  ____ \(  __  \              / )\n( \   / )| (   ) || )   ( || (    )|  | (      | (      | (   ) || () () || (   ) |  | (  \  )   ) (   | (    \/| (  \  )   _        / / \n \ (_) / | |   | || |   | || (____)|  | |      | |      | (___) || || || || (___) |  | |   ) |   | |   | (__    | |   ) |  (_)_____ ( (  \n  \   /  | |   | || |   | ||     __)  | |      | |      |  ___  || |(_)| ||  ___  |  | |   | |   | |   |  __)   | |   | |    (_____)| |  \n   ) (   | |   | || |   | || (\ (     | |      | |      | (   ) || |   | || (   ) |  | |   ) |   | |   | (      | |   ) |   _       ( (  \n   | |   | (___) || (___) || ) \ \__  | (____/\| (____/\| )   ( || )   ( || )   ( |  | (__/  )___) (___| (____/\| (__/  )  (_)       \ \ \n   \_/   (_______)(_______)|/   \__/  (_______/(_______/|/     \||/     \||/     \|  (______/ \_______/(_______/(______/              \_)')
            break
        if sleepusmaxiums.hunger>= 40:
            print("Your llama dies of starvation.")
            print('         _______           _______    _        _        _______  _______  _______    ______  _________ _______  ______                _ \n|\     /|(  ___  )|\     /|(  ____ )  ( \      ( \      (  ___  )(       )(  ___  )  (  __  \ \__   __/(  ____ \(  __  \              / )\n( \   / )| (   ) || )   ( || (    )|  | (      | (      | (   ) || () () || (   ) |  | (  \  )   ) (   | (    \/| (  \  )   _        / / \n \ (_) / | |   | || |   | || (____)|  | |      | |      | (___) || || || || (___) |  | |   ) |   | |   | (__    | |   ) |  (_)_____ ( (  \n  \   /  | |   | || |   | ||     __)  | |      | |      |  ___  || |(_)| ||  ___  |  | |   | |   | |   |  __)   | |   | |    (_____)| |  \n   ) (   | |   | || |   | || (\ (     | |      | |      | (   ) || |   | || (   ) |  | |   ) |   | |   | (      | |   ) |   _       ( (  \n   | |   | (___) || (___) || ) \ \__  | (____/\| (____/\| )   ( || )   ( || )   ( |  | (__/  )___) (___| (____/\| (__/  )  (_)       \ \ \n   \_/   (_______)(_______)|/   \__/  (_______/(_______/|/     \||/     \||/     \|  (______/ \_______/(_______/(______/              \_)')
            break
        if sleepusmaxiums.wool<=0:
                print('         _______           _______    _        _        _______  _______  _______    ______  _________ _______  ______                _ \n|\     /|(  ___  )|\     /|(  ____ )  ( \      ( \      (  ___  )(       )(  ___  )  (  __  \ \__   __/(  ____ \(  __  \              / )\n( \   / )| (   ) || )   ( || (    )|  | (      | (      | (   ) || () () || (   ) |  | (  \  )   ) (   | (    \/| (  \  )   _        / / \n \ (_) / | |   | || |   | || (____)|  | |      | |      | (___) || || || || (___) |  | |   ) |   | |   | (__    | |   ) |  (_)_____ ( (  \n  \   /  | |   | || |   | ||     __)  | |      | |      |  ___  || |(_)| ||  ___  |  | |   | |   | |   |  __)   | |   | |    (_____)| |  \n   ) (   | |   | || |   | || (\ (     | |      | |      | (   ) || |   | || (   ) |  | |   ) |   | |   | (      | |   ) |   _       ( (  \n   | |   | (___) || (___) || ) \ \__  | (____/\| (____/\| )   ( || )   ( || )   ( |  | (__/  )___) (___| (____/\| (__/  )  (_)       \ \ \n   \_/   (_______)(_______)|/   \__/  (_______/(_______/|/     \||/     \||/     \|  (______/ \_______/(_______/(______/              \_)')
                break




T1=threading.Thread(target=everything)
T2 =threading.Thread(target=growing)



T1.start()
T2.start()

T1.join()
T2.join()

print("Bye!")


