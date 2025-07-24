class Device:
    def __init__(self, brand):
        self.brand = brand
    
    def power_on(self):
        print(f"{self.brand} device is now on")

class Laptop(Device):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
    
    def show_specs(self):
        print(f"{self.brand} - {self.model}")

device1 = Device("Xiaomi")
device1.power_on()

laptop1 = Laptop("Xiaomi", "11 T")
laptop1.show_specs()

laptop1.power_on()