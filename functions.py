import random
# number=input("Type a number")

# def check(num):
#     while True:
#         if num.isalpha():
#             number=input("Invalid input,Type only numbers")
#             continue
#         elif num.isdigit()==True:
#             num=int(num)
#             if num%2==0:
#                 print(f"Your number is even")
#                 break
#             else :
#                 print("Your number is odd")
#                 break
#         else:
#             number=input("Invalid input,Type only numbers")
#             continue


# check(number)


# make a function which takes 3 number values and it will tell me which number is the biggest. 

num1=random.randint(1,10)
num2=random.randint(1,10)
num3=random.randint(1,10)
result=''
print(num1,num2,num3)
def greatest(n1,n2,n3):

    if(n1 <= n2 <= n3) or (n2 <= n1 <= n3):
        print(f"{n3} is the largest number")
    elif(n1 <= n3 <= n2) or (n3 <= n1 <= n2):
        print(f"{n2} is the largest number")
    else:
        print(f"{n1} is the largest number")
    
    # if n1>n2 and n1>n3:
    #     result=n1 
    #     print(f'{result} is the biggest number')  
    # elif n2>n1 and n2>n3:
    #     result=n2
    #     print(f'{result} is the biggest number')   
    # elif n3>n2 and n3>n1:
    #     result=n3
    #     print(f'{result} is the biggest number')  
    # elif n1==n2 and n1>n3:
    #     result=n1
    #     print(f'{result} is the biggest number')  
    # elif n3==n2 and n3>n1:
    #     result=n3
    #     print(f'{result} is the biggest number')  
    # elif n3==n1 and n3>n2:
    #     result=n3
    #     print(f'{result} is the biggest number')  
    # else:
    #     print(f"your values {n1},{n2},{n3} are all equal")



greatest(num1,num2,num3)


