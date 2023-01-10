import pygame
import math
from particles import Particle

particle_list = [Particle(10, 10, (0, 0, 255), 10, 10), Particle(10, 10, (0, 0, 255), 290, 10, -1), Particle(10, 10, (0, 0, 255), 150, 10, 0)]

pygame.init()
clock = pygame.time.Clock()

# Set up the drawing window
screen_size = 300
screen = pygame.display.set_mode([screen_size, screen_size])

running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    for i, p1 in enumerate(particle_list):
        p1.move()
        pygame.draw.circle(screen, p1.color, (p1.x, p1.y), p1.radius)
        if(p1.x + p1.radius >= screen_size or p1.x - p1.radius <= 0):
            p1.collide()
        for p2 in particle_list[i+1:]:
            dist_x = (p1.x + p1.speed) - (p2.x + p2.speed)
            dist_y = p1.x - p2.x
            if(math.hypot(dist_x, dist_y) <= p1.radius + p2.radius):
                print('invertendo sentido')
                p1.speed, p2.speed = p2.speed, p1.speed

    # Flip the display
    clock.tick(60)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()