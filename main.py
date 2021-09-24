# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------

import pygame
pygame.init()

from game import Game


# ----------------------------------------------------------------------------------------------------------------------
# CLASS
# ----------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------------------------------------------------

# window's game
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))  # width and height

# background --> import
background = pygame.image.load('assets/bg.jpg')

# generating game
game = Game()

running = True
# while the game is active
while running:

    # attaching background
    screen.blit(background, (0, -200)) # width and height

    # attaching player's image
    screen.blit(game.player.image, game.player.rect)

    # checking left / right movements
    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_a) and game.player.rect.x > 0:
        game.player.move_left()

    # updating screen
    pygame.display.flip()

    # if the player closes this window
    for event in pygame.event.get():
        # if the event == window's closed
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # keyboard key released
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False