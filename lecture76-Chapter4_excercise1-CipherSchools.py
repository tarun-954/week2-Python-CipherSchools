class Phone:
    def __init__(self, brand,model_name,price):
        self.brand=brand
        self.model_name= model_name
        self.price=max(price,0)
    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling{number}....."

class SmartPhone(Phone): #derived / child class
    def __init__(self, brand,model_name,price,ram,internal_memory,camera):
        # two ways
        Phone.__init__(self,brand,model_name,price)
        super().__int__(brand,brand,model_name,price) #uncommon way         self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=camera

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling{number}....."
phone=Phone("nokia","1100",1000)
smartphone=SmartPhone("Oneplus","s",30000,"6gb","64gb","20mp")
print(phone.full_name())
print(smartphone.full_name()+" and price is")
