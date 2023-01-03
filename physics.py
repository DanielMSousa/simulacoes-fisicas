import random
import math

class Particle:
    def __init__(self, screensize, mass, energy, color, elasticity=1):
        self.mass = mass
        self.energy = energy
        self.color = color
        self.elasticity = elasticity

        #movement related stuff
        self.radius = self.mass ** (1/2) + 1
        self.x_direction = random.uniform(-1, 1)
        self.y_direction = random.uniform(-1, 1)
        self.speed = self.calculate_speed()
        self.calculate_speed_vectors()

        #position
        min_x, max_x = screensize * 0.1, screensize * 0.9
        self.x = random.randint(min_x, max_x)
        self.y = random.randint(min_x, max_x)
    
    def calculate_speed(self):
        #v = raiz(2E/m) -> formula da energia cinética 
        return (2*self.energy/self.mass)**(1/2) * 30
    
    def calculate_speed_vectors(self):
        self.x_speed = self.speed * self.x_direction
        self.y_speed = self.speed * self.y_direction

    def draw_particle(self, f, screen):
        f(screen, self.color, (self.x, self.y), self.radius*1.2)
    
    def move_particle(self):
        self.x += self.x_speed
        self.y += self.y_speed
    
    #depois fazer uma função collide que faça isso e colocar pra essa função retornar só true ou false
    def detect_border_colision(self, screensize):
        if(self.x - self.radius <= 0 or self.x + self.radius >= screensize):
            self.x_direction *= -1
        elif(self.y - self.radius <= 0 or self.y + self.radius >= screensize):
            self.y_direction *= -1
        self.calculate_speed_vectors()
    
    def calculate_distance(self, other_particle):
        return math.dist((self.x, self.y), (other_particle.x, other_particle.y))

    def particle_collision(self, other_particle):
        if(self.radius + other_particle.radius <= self.calculate_distance(other_particle)):
            return True
