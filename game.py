# ----------------------------------------------------------------------------------------------------------------------
# IMPORT
# ----------------------------------------------------------------------------------------------------------------------

from player import Player

# ----------------------------------------------------------------------------------------------------------------------
# CLASS
# ----------------------------------------------------------------------------------------------------------------------

class Game:

    def __init__(self):
        self.player = Player()  # loading player
        self.pressed = {}