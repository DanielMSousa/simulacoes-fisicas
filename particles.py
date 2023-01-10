class Particle:
    def __init__(self, radius:float, energy:float, color, x:int, y:int, speed = 1):
        self.radius = radius
        self.energy = energy
        self.color = color
        self.x = x
        self.y = y
        self.speed = speed
    
    def move(self):
        self.x += self.speed

    def collide(self):
        self.speed = -self.speed