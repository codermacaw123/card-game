# Deck of cards.
# have a button on screen for user1 to pick a card and user2 to pick a card
# when user1 click on button1, it shows on screen : User1 card is - 4 of Spades
# when user2 click on button2, it shows on screen : User1 card is - Jack of Diamonds
# User2 wins the game.



import random,pygame,pygwidgets,sys,time


WINDOW_HEIGHT=1080
WINDOW_WIDTH=1920
BLACK = (0,0,250)
FRAMES_PER_SECOND=30
textcolor=(255, 255, 255)

pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock=pygame.time.Clock()

allcards=["2H","2D","2C","2S","3H","3D","3C","3S","4H", "4D", "4C", "4S", "5H", "5D", "5C", "5S", "6H", "6D", "6C", "6S", "7H", "7D", "7C", "7S", "8H", "8D", "8C", "8S", "9H", "9D", "9C", "9S", "10H", "10D", "10C", "10S", "JH", "JD", "JC", "JS", "QH", "QD", "QC", "QS", "KH", "KD", "KC", "KS", "AH", "AD", "AC", "AS"]
positions=[100,350,600,850,1100,1350,1600]
random.shuffle(allcards) 
computercard = allcards[0]
option1val= allcards[1]
option2val= allcards[2]
option3val= allcards[3]
option4val= allcards[4]
option5val= allcards[5]

computercard2 = allcards[7]
money=10
wager=0
err=""
selectedoption=""
m = f"Your balance is ${money}"
gamestate=False
rounds=1
buttonstate=False



random.shuffle(positions)

optioncomputer = pygwidgets.Image(window,(positions[0],300),f'images/{computercard}.jpg',)
option1=pygwidgets.Image(window,(positions[1],300),f'images/{option1val}.jpg')
option2=pygwidgets.Image(window,(positions[2],300),f'images/{option2val}.jpg')
option3=pygwidgets.Image(window,(positions[3],300),f'images/{option3val}.jpg')
option4=pygwidgets.Image(window,(positions[4],300),f'images/{option4val}.jpg')
optioncomputer2 = pygwidgets.Image(window,(positions[5],300),f'images/{computercard2}.jpg',)
option5=pygwidgets.Image(window,(positions[6],300),f'images/{option3val}.jpg')


heading=pygwidgets.DisplayText(window,(800,100),"choose your cards wisely!",fontSize=50,textColor=textcolor)
start_button=pygwidgets.TextButton(window,(1000,200),"START !",textColor=textcolor,downColor=BLACK,upColor=BLACK)
roundsText=pygwidgets.DisplayText(window,(800,200),f"Round: {rounds} ",textColor=textcolor,fontSize=40)
balance=pygwidgets.DisplayText(window,(200,200),m,textColor=textcolor,fontSize=40)
realthing=pygwidgets.TextRadioButton(window,(positions[0],700),group="chooserbuttons",text="Choose  2me",textColorDeselected=textcolor,textColorSelected=textcolor,fontSize=30)
anotherealthing=pygwidgets.TextRadioButton(window,(positions[5],700),group="chooserbuttons",text="Choose 1 me",textColorDeselected=textcolor,textColorSelected=textcolor,fontSize=30)
button1=pygwidgets.TextRadioButton(window,(positions[1],700),group="chooserbuttons",text="Choose me",textColorDeselected=textcolor,textColorSelected=textcolor,fontSize=30)
button2=pygwidgets.TextRadioButton(window,(positions[2],700),group="chooserbuttons",text="Choose me",textColorDeselected=textcolor,textColorSelected=textcolor,fontSize=30)
button3=pygwidgets.TextRadioButton(window,(positions[3],700),group="chooserbuttons",text="Choose me",textColorDeselected=textcolor,textColorSelected=textcolor,fontSize=30)
button4=pygwidgets.TextRadioButton(window,(positions[4],700),group="chooserbuttons",text="Choose me",textColorDeselected=textcolor,textColorSelected=textcolor,fontSize=30)
button5=pygwidgets.TextRadioButton(window,(positions[6],700),group="chooserbuttons",text="Choose me",textColorDeselected=textcolor,textColorSelected=textcolor,fontSize=30)

wag = pygwidgets.DisplayText(window,(300,800),"Type Wagering Amount: ",fontSize=25,textColor=textcolor)
wagering_amount=pygwidgets.InputText(window,(500,800),"",textColor="black",backgroundColor="white", fontSize=25, width=300)
errormessage=pygwidgets.DisplayText(window,(850,800),"",textColor=textcolor,fontSize=25)
winningtext = pygwidgets.DisplayText(window, (1300,200),"",textColor=textcolor,fontSize=25 )
submit=pygwidgets.TextButton(window,(550,850),"Submit Your Answer",textColor=textcolor,upColor=BLACK,downColor=BLACK,overColor=BLACK)
tryagainbutton=pygwidgets.TextButton(window,(300,550),"click here to try again",textColor=textcolor,upColor=BLACK,downColor=BLACK,overColor=BLACK,fontSize=30)
tryagaintext=pygwidgets.DisplayText(window,(250,350),f"YOU HAVE Won with {money} DO YOU WANT TO TRY AGAIN and win more??",textColor = textcolor,fontSize=30)
# tryagainbutton2 = pygwidgets.TextButton(window,(550,550),"Try Again",textColor=textcolor,upColor=BLACK,downColor=BLACK,overColor=BLACK,fontSize=30)

losingsound=pygwidgets.SoundEffect("Sounds/losing.mp3")
winningsound=pygwidgets.SoundEffect("Sounds/applause.mp3")
shuffling=pygwidgets.SoundEffect("Sounds/reshuffling.mp3")

while True:
    

    # 7 - Check for and handle events
    for event in pygame.event.get():

        # clicked the close button to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if start_button.handleEvent(event):
            gamestate=True
            pass
        if realthing.handleEvent(event):
            selectedoption = "real"
            buttonstate=True
            winningtext.hide()
        if button1.handleEvent(event):
            selectedoption = "op1"
            buttonstate=True
            winningtext.hide()
        if button2.handleEvent(event):
            selectedoption = "op2"
            buttonstate=True  
            winningtext.hide()     
        if button3.handleEvent(event):
            selectedoption = "op3"
            buttonstate=True
            winningtext.hide()
        if button4.handleEvent(event):
            selectedoption = "op4"
            buttonstate=True
            winningtext.hide()
        if button5.handleEvent(event):
            selectedoption = "op5"
            buttonstate=True
            winningtext.hide()

        if anotherealthing.handleEvent(event):
            selectedoption= "real"
            buttonstate=True        
            winningtext.hide()
        if submit.handleEvent(event):
            if buttonstate==True and wagering_amount.text!="":
                if wager>money: 
                    errormessage.setValue("You do not have that much money!")
                    wager=0
                    wagering_amount.clearText()
                elif wager<1:
                    errormessage.setValue("You have a lot of money so you sould use it rather than trying to break the game!")
                    wager=0
                    wagering_amount.clearText()
                
                else:
                    errormessage.setValue("")
                    rounds=rounds+1
                    roundsText.setValue(f"Round: {rounds}")
                    print("hullo")
                    if selectedoption=="real":
                        money=money+wager
                        m=f"Your balance is ${money}"
                        balance.setValue(m)
                        print("real thing selected")
                        random.shuffle(positions)
                        winningtext.show()
                        winningtext.setValue(f"You won last round and {wager} $.")
                        pygame.time.wait(5000)
                        shuffling.play()
                        time.sleep(4)


                        if money==0:
                            tryagainbutton.show()
                            gamestate=False
                            start_button.hide()
                            tryagaintext.setValue("You have lost horribbly, like seriously how could someone do this bad?")
                            print("you are broke")


                    else:
                        money=money-wager
                        random.shuffle(positions)
                        m=f"Your balance is ${money}"
                        balance.setValue(m)
                        winningtext.show()
                        winningtext.setValue(f"You lost last round and {wager} $.")
                        pygame.time.wait(5000)
                        shuffling.play()
                        time.sleep(4)
                        if money==0:
                            tryagainbutton.show()
                            gamestate="lost"
                            start_button.hide()
                            print("you are broke")
                            tryagaintext.setValue("You have lost horribbly, like seriously how could someone do this bad?")
                            losingsound.play()
                        print("real thing not selected")

                    button1.setValue(False)
                    button2.setValue(False)
                    button3.setValue(False)
                    button4.setValue(False)
                    realthing.setValue(False)
                    anotherealthing.setValue(False)

                    random.shuffle(positions)
                    random.shuffle(allcards)
                    computercard = allcards[0]
                    option1val= allcards[1]
                    option2val= allcards[2]
                    option3val= allcards[3]
                    option4val= allcards[4]
                    option5val = allcards[5]

                    computercard2 = allcards[7]
                    option1.replace(f'images/{option1val}.jpg')
                    option2.replace(f'images/{option2val}.jpg')
                    option3.replace(f'images/{option3val}.jpg')
                    option4.replace(f'images/{option4val}.jpg')
                    option5.replace(f'images/{option5val}.jpg')


                    optioncomputer.replace(f'images/{computercard}.jpg')
                    optioncomputer2.replace(f'images/{computercard2}.jpg')

                    option1.setLoc((positions[0],300))
                    option2.setLoc((positions[1],300))
                    option3.setLoc((positions[2],300))
                    option4.setLoc((positions[3],300))
                    option5.setLoc((positions[6],300))

                    optioncomputer.setLoc((positions[4],300))
                    optioncomputer2.setLoc((positions[5],300))
                    button1.setLoc((positions[0],700))
                    button2.setLoc((positions[1],700))                
                    button3.setLoc((positions[2],700))
                    button4.setLoc((positions[3],700))
                    button5.setLoc((positions[6],700))

                    realthing.setLoc((positions[4],700))
                    anotherealthing.setLoc((positions[5],700))
                    realthing.value=False

                    option1.value=False
                    option2.value=False
                    option3.value=False
                    option4.value=False
                    option5.value=False

                    
                    buttonstate=False


        if tryagainbutton.handleEvent(event):
                rounds=1
                money=10
                wager=0
                gamestate=True
                wagering_amount.clearText()
                buttonstate=False
                
          
               
                
                

                
            
            
       
            
        if rounds>=11:
           gamestate="lost"
           
        #    tryagainbutton2.show()
           tryagaintext.show()
           winningsound.play()
           rounds=1
           time.sleep(3)

       
        # print(wager)
        # print(f"{money}+is yuour money")
        if wagering_amount.handleEvent(event):
            wager=wagering_amount.getValue()
            wager=int(wager)
            print(f"{wager} is your wager")
            
       
        if gamestate==True:
            option1.show()
            start_button.hide()
            option2.show()
            option3.show()
            option4.show()
            option5.show()
            

            button1.show()
            button2.show()
            button3.show()
            button4.show()
            button5.show()

            optioncomputer.show()
            optioncomputer2.show()
            realthing.show()
            anotherealthing.show()

            wagering_amount.show()
            submit.show()
            balance.show()
            wag.show()
            # tryagainbutton2.hide()
            tryagainbutton.hide()
            errormessage.show()
            roundsText.show()
            tryagaintext.hide()

        elif gamestate==False: 
            errormessage.hide()
            wag.hide()
            option1.hide()
            option2.hide()
            option3.hide()
            option4.hide()
            button1.hide()
            button2.hide()
            button3.hide()
            button4.hide()
            option5.hide()
            winningtext.hide()

            button5.hide()
            anotherealthing.hide()

            optioncomputer.hide()
            optioncomputer2.hide()
            optioncomputer.hide()
            realthing.hide()
            wagering_amount.hide()
            balance.hide()
            roundsText.hide()
            submit.hide()
             
            tryagaintext.hide()
            tryagainbutton.hide()
            # tryagainbutton2.hide()
        
        elif gamestate=="lost": 
            errormessage.hide()
            wag.hide()
            option1.hide()
            option2.hide()
            option3.hide()
            option4.hide()
            option5.hide()

            optioncomputer2.hide()
            button1.hide()
            button2.hide()
            button3.hide()
            button4.hide()
            button5.hide()
            winningtext.hide()

            optioncomputer.hide()
            realthing.hide()
            anotherealthing.hide()
            wagering_amount.hide()
            balance.hide()
            roundsText.hide()
            submit.hide()
            if money>0:
            
                # tryagainbutton2.show()
                tryagaintext.show()
                tryagainbutton.show()
            else:
                tryagaintext.show()
                
                tryagainbutton.show()
                # tryagainbutton2.hide()

        
       
  
    

    window.fill(BLACK)

    wag.draw()
    heading.draw()
    start_button.draw()
    option1.draw()
    option2.draw()
    option3.draw()
    option5.draw()

    option4.draw()
    button1.draw()
    button2.draw()
    button3.draw()
    button4.draw()
    button5.draw()

    realthing.draw()
    anotherealthing.draw()
    errormessage.draw()
    optioncomputer.draw()
    optioncomputer2.draw()
    wagering_amount.draw()
    submit.draw()
    balance.draw()
    tryagainbutton.draw()
    tryagaintext.draw()
    roundsText.draw()
    winningtext.draw()
  


    
    balance.setValue(f"Your balance is ${money}")
    
   


    pygame.display.update()


    clock.tick(FRAMES_PER_SECOND)


def game():
    pass