class Manu:
    def __init__(self, identity, location):
        self.identity = identity
        self.location = location
    def describe(self):
        print(f"Identity: {self.identity} - Location: {self.location} ")
        
class Device(Manu):
    def __init__ ( self, name, price, identity, location):
        self.name = name
        self.price = price
        super().__init__(identity,location)
    def describe(self):
        print(f"Name: {self.name} - Price: {self.price} ")
        super().describe()
    
dev1 = Device(name="mouse", price=2.5, identity=9725, location="Vietnam")
dev1.describe()
print()
dev2 = Device(name="monitor", price=12.5, identity=11, location="Germany")
dev2.describe()