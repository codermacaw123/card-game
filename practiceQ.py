# num of steps= 4
# steps = 1, 2, 3, 4
# (1,1,1,1) (2,2) (3,1) (1,3) (2,1,1) (1,2,1) (1,1,2)
# There are 8 ways to reach the top
#
# from terminalplot import plot

# # x = range(0, 1000, 1)
# # y = [i**3-5 for i in x]
# # plot(x,y)

# def sequence():
#     while True:
#         number = int(input("Type the amount of steps: ")) 
       
#         if number<=0:
#             print("0")
            
#         elif number==1:
#             print("1")
        
#         elif number==2:
#             print("2")
           
#         else:
         
#             finalnumber=number*3-5
#             print(finalnumber)
      
    
# sequence()






# A group of prisoners is arranged in a circle and numbered from 1 to n(ask user). 
# Starting from the first prisoner, every second prisoner is eliminated (removed from the circle) until only one remains. 
# Write a Python function to find the position of the last prisoner standing.
# number = int(input("Enter the number of people: "))

# def josephus_iterative(n, k):
#     result = 0  # Start with the base case for 1 person
#     for i in range(2, n + 1):  # Compute positions for 2 to n
#         result = (result + k) % i
#     print(f"The safe position is: {result + 1}")  # Output the 1-based index

# # Call the function with step size k=2
# josephus_iterative(number, 2)







# Make a electricity bill calculator model:
# For the first 100 units, the rate is $0.5 per unit.
# For the second 100 units, the rate is $0.75 per unit.
# For the third 100 units, the rate is $1.20 per unit.
# For anything more than 300 units, the rate is $1.50 per unit.

# Ask user what was their monthly unit consumption and give back the bill amount as answer.
# units = 450 ---> 470$
units = int(input())
def electric_bill_calculator(units):
    if units<=100:
        bill = units*0.5
    elif units<=200:
        bill= (100*0.5)+((units-100)*0.75)
    elif units<=300:
        bill=(100*0.5)+(100*0.75)+((units-200)*1.2)
    else:
        bill=((100*0.5)+(100*0.75)+(100*1.2)+((units-300)*1.5))
    print(bill)
electric_bill_calculator(units)
