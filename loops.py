# lis=[1,2,3,4,5,6,7,8,9]
# Len=9
# num=int(input("give me num"))

# # write a program to calculate the sum of all numbers from 1 to a given number which user passed.
# # for i in lis:
# #     print(i)
# def adding(num):
#     # nums=[]
#     # for i in range(1,num+1):
#     #     nums.append(i)
#     #     print(nums)
#     sum = 0
#     for i in range(1,num+1):
#         sum=sum+i
#     print(sum)
# adding(num)


# ask = input("Type a number of a string")


# def check(n):
#     r = ""
#     for i in ask:
#         r = i+r

#     if ask == r :
#         print("it is !")
#     else :
#         print("It is not")

# check(ask)


# stars=""
# print(stars)
# for i in range(1,10,2):
#     # stars="**"+stars
  
#     for x in range(1,i):
#         stars="**"+stars
#         print(stars)



    

# while True:
#     birthDate=input("Please enter your birthday in DD/MM/YYYY format")
#     if birthDate[2]=='/' and  birthDate[5]=='/' and len(birthDate)==10 :
#         birthYear=birthDate[6:]
#         birthYear=int(birthYear)
#         if birthYear%4==0:
#             print("You were born in a leap year")
#             break
#         if birthYear==2012:
#             print("The world was supposed to end")
#         if birthYear==2020:
#             print("coronavirus here I come!!")
#         if birthYear==2011:
#             print("You were born when I was!")

#     else:
#         continue
            
happy_words = ['great','good','fun','exciting','enjoyed','exciting','thriller']
sad_words=['bad','unenjoyable','horrible']
user_input = input('how was the movie?')

thingy= ''

for i in  happy_words:    
    if i in user_input:
     
        print('The user response was positive')
    else: 
        thingy="yes"
for i in  sad_words:  
    if i in user_input:
     
        print('The user response was not positive')
    else:
        thingy='yes'

if thingy=='yes':
    print(' I am a little dumb for now')
        
    


