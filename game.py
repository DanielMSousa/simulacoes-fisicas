import pygame
from physics import Particle
import random
import numpy as np
import time

pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
screen_size = 600
screen = pygame.display.set_mode([screen_size, screen_size])

#p = Particle(30, 1, (0, 0, 255))

error = 10**(-8)

def change_particle(p):
    #for p in particle_list:
    p.move_particle()
    p.draw_particle(pygame.draw.circle, screen)
    p.detect_border_colision(screen_size)

cp = np.vectorize(change_particle)

i = 0
particle_list = []
qtd = 300
while(i < qtd):
    #m = 30
    m = random.randint(20, 30)
    c = (0, 50, 200)
    energy = 1
    particle_list.append(Particle(screen_size, m, energy, c))
    i += 1

#particle_list = np.array(particle_list)

for p in particle_list:
    p.draw_particle(pygame.draw.circle, screen)

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    #cp(particle_list)
    for p in particle_list:
        change_particle(p)

    for i, p1 in enumerate(particle_list): 
        dl = []
        for p in particle_list:
            if(p1 is not p):
                if((p1.x - p.x) ** 2 + (p1.y - p.y) ** 2) ** (1/2) - (p1.radius + p.radius) <= error:

                    #colisão perfeitamente inelástica
                    p1.x_speed = 0
                    p1.y_speed = 0
                    p.y_speed = 0
                    p.x_speed = 0

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()