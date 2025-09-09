class LaptopBattery:
    def __init__(self, level = 100):
        self.__level = level
    
    @property
    def level(self):
        return self.__level

    def drain(self, amount):
        if amount > self.__level:
            print("Battery empty!")
            self.__level = 0
        else:
            self.__level -= amount
    
    def charge(self):
        self.__level = 100
    
