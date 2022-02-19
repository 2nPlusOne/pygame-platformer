import pygame
from settings import *
import utils

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE / 2, TILE_SIZE))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft=pos)
        self.collision_sprites = collision_sprites

        # Player movement
        self.direction_x = 0 # -1 = left, 1 = right, 0 = none
        self.velocity = pygame.math.Vector2()
        self.speed = MAX_PLAYER_SPEED

        # Jumping
        self.jumps_remaining = MAX_JUMPS
        self.is_grounded = False
        self.was_grounded = False
        self.is_jumping = False
        self.jump_pressed = False
        self.current_gravity = GRAVITY
        
        self.jump_gravity = (2 * MAX_JUMP_HEIGHT) / (TIME_TO_JUMP_APEX ** 2)
        self.fall_gravity = self.jump_gravity * FALL_GRAVITY_MULTIPLIER
        self.jump_velocity = ((-2 * MAX_JUMP_HEIGHT) / TIME_TO_JUMP_APEX) - self.fall_gravity

        # Time
        self.air_timer = 0
        self.est_delta_time = 1 / FPS
        self.last_frame_ticks = 0 # Not used if using estimated delta_time (1/FPS)
    
    def process_input(self, events):
        """Process input events. This method is called by Level, which passes in the events from the main game loop."""
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # Move left
                    self.direction_x = -1
                if event.key == pygame.K_RIGHT: # Move right
                    self.direction_x = 1
                if event.key == pygame.K_UP: # Jump
                    self.jump_pressed = True
                    self.try_jump()
                if event.key == pygame.K_g: # Invert gravity just for fun
                    self.fall_gravity = -self.fall_gravity
                    self.current_gravity = -self.current_gravity

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.direction_x < 0:
                    self.direction_x = 0
                if event.key == pygame.K_RIGHT and self.direction_x > 0:
                    self.direction_x = 0
                if event.key == pygame.K_UP:
                    self.jump_pressed = False

    def try_jump(self):
        """Conditionally applies jumping force to the player."""
        jump_not_allowed = not (self.jumps_remaining > 0 and 
                                (self.is_grounded or self.is_jumping or self.air_timer < COYOTE_TIME))
        if jump_not_allowed: return
        self.is_jumping = True
        self.jumps_remaining -= 1
        self.current_gravity = self.jump_gravity
        self.velocity.y = self.jump_velocity
        

    def move(self):
        """Move the player and apply collisions."""
        self.velocity.y += self.current_gravity
        
        target_velocity = pygame.math.Vector2(self.direction_x * self.speed, self.velocity.y)
        self.velocity = utils.pygame_vector2_smooth_damp(self.velocity, target_velocity, SMOOTH_TIME, self.est_delta_time)
        self.velocity.x = 0 if abs(self.velocity.x) < 2*SMOOTH_TIME else self.velocity.x

        # Horizontal movement and collisions
        self.rect.x += self.velocity.x
        for sprite in self.collision_sprites.sprites():
            if not sprite.rect.colliderect(self.rect): continue
            # Right collision
            elif abs(self.rect.right - sprite.rect.left) < COLLISION_TOLERANCE and self.velocity.x > 0:
                self.rect.right = sprite.rect.left
            # Left collision
            elif abs(self.rect.left - sprite.rect.right) < COLLISION_TOLERANCE and self.velocity.x < 0:
                self.rect.left = sprite.rect.right
            self.velocity.x = 0
            break
        
        # Vertical movement and collisions
        # Since vertical movement can be potentially a lot faster than horizontal due to gravity,
        # we need to check for collisions as we go each frame, instead of after moving by the velocity.
        for i in range(abs(int(self.velocity.y))):
            collided = False
            self.rect.y += abs(self.velocity.y) / self.velocity.y
            for sprite in self.collision_sprites.sprites():
                if not sprite.rect.colliderect(self.rect): continue
                # Bottom collision
                elif abs(self.rect.bottom - sprite.rect.top) < COLLISION_TOLERANCE and self.velocity.y > 0:
                    self.rect.bottom = sprite.rect.top
                # Top collision
                elif abs(self.rect.top - sprite.rect.bottom) < COLLISION_TOLERANCE and self.velocity.y < 0:
                    self.rect.top = sprite.rect.bottom
                self.velocity.y = 0
                collided = True
                break
            if collided: break
        
        # Set gravity to fall gravity scale if we're falling or not holding jump
        if (not self.is_grounded and (not self.jump_pressed or self.velocity.y > 0)):
            self.current_gravity = self.fall_gravity

    def set_grounded(self):
        """Moves the player down 1 pixel and checks for a collision."""
        self.rect.y += 1
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if not abs(self.rect.bottom - sprite.rect.top) < COLLISION_TOLERANCE: continue
                self.is_grounded = True
                self.was_grounded = True
                self.is_jumping = False
                self.jumps_remaining = MAX_JUMPS
                break
            else:
                self.is_grounded = False
                left_ground_this_frame = self.was_grounded and not self.is_grounded
                if not left_ground_this_frame: continue
                self.air_time_start = pygame.time.get_ticks()
                self.was_grounded = False
        self.rect.y -= 1

    def handle_air_timer(self):
        """Resets air timer if grounded, otherwise adds the delta time."""
        self.air_timer = 0 if self.is_grounded else round(self.air_timer + self.est_delta_time, 2)


    def update(self):
        """Update the player."""
        self.handle_air_timer()
        self.move()
        self.set_grounded()
        
    # Zombie method, only used if I decide I need perfect delta time (should probably remove this...)
    def update_real_delta_time(self):
        """Update the delta time."""
        self.est_delta_time = (pygame.time.get_ticks() - self.last_frame_ticks) / 1000
        self.last_frame_ticks = pygame.time.get_ticks()