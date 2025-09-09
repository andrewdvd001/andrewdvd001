class Bird:
    def speak(self):
        print("Some generic bird sound")

class Parrot(Bird):
    def speak(self):
        print("Squawk! I'm a parrot!")

class Crow(Bird):
    def speak(self):
        print("Caw! I'm a crow")

def make_it_speak(bird):
    bird.speak()

list_of_different_bird = [Crow(), Parrot()]

for bird in list_of_different_bird:
    make_it_speak(bird)