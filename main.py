import pygame
from background import Background
from mouse import Mouse

pygame.init()

WIDTH, HEIGHT = 500, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lanci Markova")
pygame.display.set_icon(pygame.image.load("mouse.png"))

background = Background(WIDTH, HEIGHT)
player = Mouse("mouse.png", 202.5, 362.5, 75, 75, background)

key_pressed = False

running = True

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_k]: 
        if not key_pressed:
            background.walls()
            background.calculate_probability(player)
            key_pressed = True
    elif keys[pygame.K_w]: 
        if not key_pressed:
            player.move_up(background)
            background.calculate_probability(player)
            key_pressed = True
    elif keys[pygame.K_s]: 
        if not key_pressed:
            player.move_down(background)
            background.calculate_probability(player)
            key_pressed = True
    elif keys[pygame.K_a]: 
        if not key_pressed:
            player.move_left(background)
            background.calculate_probability(player)
            key_pressed = True
    elif keys[pygame.K_d]: 
        if not key_pressed:
            player.move_right(background)
            background.calculate_probability(player)
            key_pressed = True
    else:
        key_pressed = False

    background.display(screen)
    player.display(screen)
    background.write_text(screen)

    pygame.display.flip()   

pygame.quit()