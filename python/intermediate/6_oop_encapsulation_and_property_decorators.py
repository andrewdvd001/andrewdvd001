class LaptopBattery:
    def __init__(self, level = 100):
        self.__level = level
    
    @property
    def level(self):
        return f"Current battery level is {self.__level}%"

    def drain(self, amount):
        if amount > self.__level:
            print("Battery empty!")
            self.__level = 0
        else:
            self.__level -= amount
    
    def charge(self):
        self.__level = 100
    
battery = LaptopBattery()
print(battery.level)       # 100
battery.drain(30)
print(battery.level)       # 70
battery.drain(100)
print(battery.level)       # 0
battery.charge()
print(battery.level)       # 100
