from cars import Car

car_1= Car("Lincoln","Nautilus",1100,78000,400,4.7,"Gasoline",7.8,"6 seconds","inline 4")

car_2= Car("Land Rover","Velar",1500,100000,700,4.9,"Gasoline",10,"5 seconds","inline 6")

car_3= Car("BMW","X5",1800,120000,400,5.0,"PHEV",9.5,"4 seconds","inline 6")

car_4= Car("Lexus","TX",1200,85000,600,5.1,"Gasoline",8.8,"6 seconds","inline 4")

car_5= Car("Cadillac","Lyriq",1400,10000,400,5.0,"electric",9,"6 seconds","Dual motors")

def comparison():
    choice=input("What quality of the cars would you like to know?")
    
    if choice=="insurance":
        print(car_1.make,car_1.model,car_1.lease_price,car_1.insurance)
        print(car_3.make,car_3.model,car_3.lease_price,car_3.insurance)
        print(car_5.make,car_5.model,car_5.lease_price,car_5.insurance)
        print(car_4.make,car_4.model,car_4.lease_price,car_4.insurance)
        print(car_2.make,car_2.model,car_2.lease_price,car_2.insurance)
    if choice=="price":
        print(car_1.make,car_1.model,car_1.lease_price,car_1.insurance)
        
        print(car_5.make,car_5.model,car_5.lease_price,car_5.insurance)
        print(car_4.make,car_4.model,car_4.lease_price,car_4.insurance)
        print(car_2.make,car_2.model,car_2.lease_price,car_2.insurance)
        print(car_3.make,car_3.model,car_3.lease_price,car_3.insurance)
    if choice=="rating":
        print(car_2.make,car_2.model,car_2.lease_price,car_2.insurance,car_2.rating)
        
        print(car_3.make,car_3.model,car_3.lease_price,car_3.insurance,car_3.rating)
        print(car_4.make,car_4.model,car_4.lease_price,car_4.insurance,car_4.rating)

        print(car_5.make,car_5.model,car_5.lease_price,car_5.insurance,car_5.rating)
        print(car_1.make,car_1.model,car_1.lease_price,car_1.insurance,car_1.rating)
    
    if choice=="electric":
    

        print(car_5.make,car_5.model,car_5.lease_price,car_5.insurance,car_5.rating)

        
        
        
    
comparison()