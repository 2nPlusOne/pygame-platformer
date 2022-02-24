import pygame
from settings import *
from player import Player
from tile import Tile

class Level:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()

        self.player = None

        # Sprite groups setup
        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup_level()

    def setup_level(self):
        """Generate the level from the level map."""
        for i, row in enumerate(LEVEL_MAP):
            for j, tile in enumerate(row):
                x_pos = j * TILE_SIZE
                y_pos = i * TILE_SIZE
                if tile == 'X':
                    Tile((x_pos, y_pos), (self.collision_sprites, self.visible_sprites))
                elif tile == 'P':
                    self.player = Player((x_pos, y_pos), (self.visible_sprites, self.active_sprites), self.collision_sprites)

    def run(self, events):
        """Run the level (entire game)."""
        # Have player process the input events
        self.player.process_input(events)

        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.draw(self.display_surf)

class CameraGroup(pygame.sprite.Group):
    """A sprite group that follows the camera."""
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2(100, 300)
        self.display_surface = pygame.display.get_surface()

        # Create the camera box rect
        cam_left = CAMERA_BORDERS['left']
        cam_top = CAMERA_BORDERS['top']
        cam_width = self.display_surface.get_width() - (CAMERA_BORDERS['left'] + CAMERA_BORDERS['right'])
        cam_height = self.display_surface.get_height() - (CAMERA_BORDERS['top'] + CAMERA_BORDERS['bottom'])
        
        self.cam_rect = pygame.Rect(cam_left, cam_top, cam_width, cam_height)
    
    def set_offset_centered(self, player):
        """Set the camera offset to be centered on the player."""
        half_width = self.display_surface.get_width() / 2
        half_height = self.display_surface.get_height() / 2

        self.offset.x = player.rect.centerx - half_width
        self.offset.y = player.rect.centery - half_height

    def set_offset_camera_box(self, player):
        """Set the camera offset to keep the player within the camera box borders."""

        # Set the camera rect position
        if player.rect.left < self.cam_rect.left:
            self.cam_rect.left = player.rect.left
        if player.rect.right > self.cam_rect.right:
            self.cam_rect.right = player.rect.right
        if player.rect.top < self.cam_rect.top:
            self.cam_rect.top = player.rect.top
        if player.rect.bottom > self.cam_rect.bottom:
            self.cam_rect.bottom = player.rect.bottom

        # Calculate camera offset
        self.offset = pygame.math.Vector2(
            self.cam_rect.left - CAMERA_BORDERS['left'], 
            self.cam_rect.top - CAMERA_BORDERS['top'])

    def custom_draw(self, player):
        """Draw all sprites in the group."""
        # Get the camera offset
        self.set_offset_camera_box(player)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)