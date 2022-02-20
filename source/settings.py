LEVEL_MAP = [
'                                           ',
'                                           ',
'                                   XX      ',
' XX    XXX           XX                 XX ',  
' XX P                          XX          ',
' XXXX          XX        XX                ',
' XXXX        XX                            ',
' XX     X  XXXX    XX XX               XX  ',
'        X  XXXX    XX XXX     XXX          ',
'     XXXX  XXXXXX  XX XXXX     XXXX   XXXXX',
'XXXXXXXXX  XXXXXX  XX XXXX       XXX  XXXXX']

LEVEL_MAP2 = [
'                                        ',
'                                        ',
'                                        ',
'  XXXXX                                 ',
'  X               XXXXXXXXX             ',
'  X                                     ',
'  XXXXXXXX                              ',
'                             XXXXXX     ',
'            XXXX                        ',
'              XXXXXX                    ',
'               XXX                      ',
'               XXX XXXXXXX              ']

# Game initialization settings
TITLE = "Pygame Platformer"
TILE_SIZE = 64           # Pixel width and height of each tile
SCREEN_WIDTH = 1280      # Pixel width of the game window
SCREEN_HEIGHT = 720      # Pixel height of the game window
FPS = 60                 # Frames per second
EST_DELTA_TIME = 1 / FPS # Estimated delta time

# Player settings
MAX_PLAYER_SPEED = 8                # Maximum speed of the player in pixels per frame
SMOOTH_TIME = 0.1                   # Time in seconds to smooth player movement
COLLISION_TOLERANCE = TILE_SIZE / 4 # Tolerance for collisions in pixels

# Jumping
COYOTE_TIME = 5 * (1 / FPS)            # Frames of coyote time * time duration of 1 frame
JUMP_BUFFER_TIME = 5 * (1 / FPS) # Frames of jump input buffer * time duration of 1 frame
MAX_JUMPS = 2                          # Number of jumps the player has until grounded
MAX_JUMP_HEIGHT = 2 * TILE_SIZE        # Pixel height of the player's jump
TIME_TO_JUMP_APEX = 0.35 * FPS         # Number of frames it takes to reach the apex of the jump
FALL_GRAVITY_MULTIPLIER = 1.8          # Multiplier for gravity when falling

# Colors
BG_COLOR = '#1e1e1e'     # Background color
PLAYER_COLOR = '#007acc' # Player color
TILE_COLOR = '#858585'   # Tile color

# Camera
CAMERA_BORDERS = {
    'left': SCREEN_WIDTH / 3,  # Pixel width of the left border
    'right': SCREEN_WIDTH / 3, # Pixel width of the right border
    'top': 100,                # Pixel height of the top border
    'bottom': 150,             # Pixel height of the bottom border
}