# Class with inheritance
class Vehicle:
    def __init__(self, name): self.name = name
    def move(self): print(f"{self.name} is moving")

class Hoverboard(Vehicle):
    def move(self): print(f"{self.name} is gliding silently")

h = Hoverboard("Saba's Hoverboard")
h.move()
