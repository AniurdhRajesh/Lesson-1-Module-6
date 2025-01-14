import pygame
import sys
pygame.init()
width, height = 1000, 2000
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Pygame Window with Image')

image_path = 'wp4882992.jpg'
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
