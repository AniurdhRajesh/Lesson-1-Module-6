import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame Rectangle and Text Example')

font = pygame.font.Font(None, 36) 
text = font.render('Hello, Pygame!', True, (255, 255, 255))
text_rect = text.get_rect(center=(400, 50))

rect = pygame.Rect(300, 200, 200, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit()

    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, (0, 125, 255), rect)  
    screen.blit(text, text_rect) 
    pygame.display.flip()
