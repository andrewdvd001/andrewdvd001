class Appliance:
    def turn_on(self):
        print("Appliance is now running.")

class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing machine is now washing clothes.")

Appliance1 = Appliance()
WashingMachine1 = WashingMachine()

Appliance1.turn_on()
WashingMachine1.turn_on()