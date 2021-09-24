# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------

import pygame
pygame.init()


# ----------------------------------------------------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------------------------------------------------

# window's game
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))  # width and height

# background --> import
background = pygame.image.load('assets/bg.jpg')

running = True

# while the game is active

while running:

    # attaching background
    screen.blit(background, (0, -200)) # width and height

    # updating screen
    pygame.display.flip()

    # if the player closes this window
    for event in pygame.event.get():
        # if the event == window's closed
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
