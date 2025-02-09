class Calculation:

    def __init__(self, num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2
    
    def subraction(self):
        print(f"{self.num1} minus {self.num2} is {self.num1-self.num2}")
    def addition(self):
        print(f"{self.num1} plus {self.num2} is {self.num1+self.num2}")
    
    



prob1 = Calculation(20,10)
prob1.subraction()
prob1.addition()

