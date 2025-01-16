import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
rect = pygame.Rect(400, 300, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()

    keys = pygame.key.get_pressed()
    rect.move_ip((keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]), (keys[pygame.K_DOWN] - keys[pygame.K_UP]))
    color = (0, 0, 255) if rect.left < 0 or rect.right > 800 or rect.top < 0 or rect.bottom > 600 else (0, 255, 0)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, rect)
    pygame.display.flip()
