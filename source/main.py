import pygame, sys
from settings import *
from level import Level

# TODO:
# - import animations CHECK
# - animate the player's state CHECK
# - fix player clipping into the wall when exiting jump state
# - create an animator class
# - create an enum for the animator states
# - create an animator state machine?
# - create a state machine for the player state?
# - create an enum for the player states?

# Pygame Initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), vsync=True)
clock = pygame.time.Clock()
pygame.display.set_caption(TITLE)

level = Level()

# Main game loop
while True:
    # Cache events to pass to the level
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)

    # Run the level, and pass events to it
    level.run(events)

    pygame.display.update()
    clock.tick(FPS)