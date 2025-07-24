class SpeedMonitor:
    def __init__(self, speed = 0):
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        if value < 0 or value > 180:
            print("Speed must be between 0 and 180")
        else:
            self.__speed = value

    def show_speed(self):
        print(f"Current speed: {self.__speed}")

car1 = SpeedMonitor()
car1.speed = 90
car1.show_speed()
car1.speed = -10
car1.show_speed()
car1.speed = 200
car1.show_speed()
car1.speed = 120
car1.show_speed()