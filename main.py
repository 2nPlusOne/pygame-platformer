import pygame, sys
from settings import *
from level import Level

# TODO:
# - Add better jumping using time to apex and jump height
# - Add variable jump height - [CHECK]

# Pygame Initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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