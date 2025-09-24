class Wildlife:
    def habitat(self):
        pass

class Mammal(Wildlife):
    def habitat(self):
        return "Mammals ain't same to birds"
class Bird(Wildlife):
    def habitat(self):
        return "Birds are nothing like mammals"
    
#creating subclass objects
mammal = Mammal()
bird = Bird()

#printing each separately
print("Mammals:")
print(mammal.habitat())
print("\nBird:")
print(bird.habitat())