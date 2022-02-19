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
TILE_SIZE = 64
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Player settings
MAX_PLAYER_SPEED = 10
SMOOTH_TIME = 0.1
COLLISION_TOLERANCE = TILE_SIZE / 2
GRAVITY = .8

# Jumping
COYOTE_TIME = 0.2
MAX_JUMPS = 2
MAX_JUMP_HEIGHT = 2 * TILE_SIZE
TIME_TO_JUMP_APEX = 0.35 * FPS
FALL_GRAVITY_MULTIPLIER = 1.8

# Colors
BG_COLOR = '#1e1e1e'
PLAYER_COLOR = '#007acc'
TILE_COLOR = '#858585'

# Camera
CAMERA_BORDERS = {
    'left': SCREEN_WIDTH / 3,
    'right': SCREEN_WIDTH / 3,
    'top': 100,
    'bottom': 150,
}