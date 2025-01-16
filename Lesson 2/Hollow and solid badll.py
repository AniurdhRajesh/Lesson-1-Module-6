import pygame
pygame.init()
width,height=800,600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Circle')

white = (255, 255, 255)
green = (0, 255, 0)

center_solid = (400, 300)
radius_solid = 50

center_hollow = (600, 300)
radius_hollow = 70
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(white)
    pygame.draw.circle(screen, green, center_solid, radius_solid)
    pygame.draw.circle(screen, green, center_hollow, radius_hollow, 3)
    pygame.display.flip()