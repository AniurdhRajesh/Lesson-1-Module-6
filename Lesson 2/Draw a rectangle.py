import pygame
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rectangle')
black = (0, 0, 0)
blue = (0, 125, 255)
left = 300
top = 200
width_rect = 200
height_rect = 150

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen, blue, (left, top, width_rect, height_rect))
    pygame.display.flip()