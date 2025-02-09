import pygame,pygwidgets,sys
# Make a electricity bill calculator model:
# For the first 100 units, the rate is $0.5 per unit.
# For the second 100 units, the rate is $0.75 per unit.
# For the third 100 units, the rate is $1.20 per unit.
# For anything more than 300 units, the rate is $1.50 per unit.

# Ask user what was their monthly unit consumption and give back the bill amount as answer.
# units = 450 ---> 470$
# units = int(input())
# def electric_bill_calculator(units):
#     if units<=100:
#         bill = units*0.5
#     elif units<=200:
#         bill= (100*0.5)+((units-100)*0.75)
#     elif units<=300:
#         bill=(100*0.5)+(100*0.75)+((units-200)*1.2)
#     else:
#         bill=((100*0.5)+(100*0.75)+(100*1.2)+((units-300)*1.5))
#     print(bill)
# electric_bill_calculator(units)

# 1 - main code

# def electric_bill_calculator(units,multiplier):
    # if units<=100:
    #     bill = units+multiplier
    #     print("helolo")
    # elif units<=200:
    #     bill= units+multiplier
    #     print("helolo")
    # elif units<=300:
    #     bill=units+multiplier
    #     print("helolo")
    # else:
    #     bill=units+multiplier
    #     print("helolo")
    # return bill

    # if units<=100:
    #     bill = units*0.5*multiplier
    #     print("helolo")
    # elif units<=200:
    #     bill= (100*0.5*multiplier)+((units-100)*0.75*multiplier)
    #     print("helolo")
    # elif units<=300:
    #     bill=(100*0.5*multiplier)+(100*0.75*multiplier)+((units-200)*1.2*multiplier)
    #     print("helolo")
    # else:
    #     bill=((100*0.*multiplier)+(100*0.75*multiplier)+(100*1.2*multiplier)+((units-300)*1.5*multiplier))
    #     print("helolo")
    # return bill



# 2 - Define constants

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
BLACK = (0,0,250)
FRAMES_PER_SECOND = 0

# 3 - Initialize the world
pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock=pygame.time.Clock()


# 4 - Load assets: image(s), sound(s),  etc.

# 5 - Initialize variables

heading = pygwidgets.DisplayText(window,(150,50),"Bill Calculator", fontSize=60,textColor="lime", )
questiontext = pygwidgets.DisplayText(window,(100,200),"What is your montly unit consumption?",fontSize=30 ,textColor="lime")
inputtext= pygwidgets.InputText(window,(100,300),width=200,fontSize=30,textColor="lime",backgroundColor="blue",initialFocus=True,)
greeneenergy=pygwidgets.TextRadioButton(window,(100,350), "energyprovider",text="green energy",textColorDeselected="lime",textColorSelected="lime",fontSize=30)
nuclearenergy=pygwidgets.TextRadioButton(window,(100,370), "energyprovider",text="nuclear energy",textColorDeselected="lime",textColorSelected="lime",fontSize=30)
coaleenergy=pygwidgets.TextRadioButton(window,(100,390), "energyprovider",text="coal energy",textColorDeselected="lime",textColorSelected="lime",fontSize=30)
textbutton= pygwidgets.TextButton(window,(100,500),"calculate total cost",300,40,textColor="lime",downColor="blue",fontSize=40,upColor="blue",overColor="blue")
answertext=pygwidgets.DisplayText(window,(150,600),"",fontSize=30,textColor="lime")
units=""
ep=""
bill = 0
nuclear=0.4
coal=0.55
green=0.75
multiplier=0
billans = ''

# 6 - Loop forever

while True:
    

    # 7 - Check for and handle events
    for event in pygame.event.get():

        # clicked the close button to quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if inputtext.handleEvent(event):
            units=inputtext.getValue()
            units = int(units)
            print("I am here")
        
        if nuclearenergy.handleEvent(event):
            ep="nuclear"
            multiplier=0.9
            
        if coaleenergy.handleEvent(event):
            ep="coal"
            multiplier=1.1
        if greeneenergy.handleEvent(event):
            ep="green"
            multiplier=1.2
        
        if textbutton.handleEvent(event):
            
            if units<=100:
                bill = units*0.5*multiplier
            elif units<=200:
                bill= (100*0.5*multiplier)+((units-100)*0.75*multiplier)
            elif units<=300:
                bill=(100*0.5*multiplier)+(100*0.75*multiplier)+((units-200)*1.2*multiplier)
            else:
                bill=((100*0.*multiplier)+(100*0.75*multiplier)+(100*1.2*multiplier)+((units-300)*1.5*multiplier))
            
            billans = f'''Your total energy bill for this month's {units} units consumption is {bill}, 
            we know where you live so then do no attempt fraud '''
            answertext.setValue(billans)
           




    # 8 - Do any "per frame" actions



    # 9 - Clear the window
    window.fill(BLACK)



    # 10 - Draw all window elements
    heading.draw()
    questiontext.draw()
    inputtext.draw()
    textbutton.draw()
    answertext.draw()
    nuclearenergy.draw()
    greeneenergy.draw()
    coaleenergy.draw()


    # 11 - Update the window
    pygame.display.update()


    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)



       
 