import pygame
from math import inf

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def pygame_vector2_smooth_damp(current: pygame.math.Vector2, 
                        target: pygame.math.Vector2, 
                        smooth_time: float, delta_time: float,
                        current_velocity=pygame.math.Vector2(0, 0)) -> pygame.math.Vector2:
    """
    Gradually changes a vector towards a desired goal over time.
    :param current: Current position.
    :param target: Position we're trying to reach.
    :param smooth_time: Approximately the time it will take to reach the target.
    :param delta_time: The realtime since the last call to this function.
    :param current_velocity: Current velocity, this value is modified by the function every time you call it.
    :return: New position.
    """
    max_speed = inf

    smoothTime = max(0.0001, smooth_time)
    omega = 2 / smoothTime

    x = omega * delta_time
    exp = 1 / (1 + x + 0.48 * x * x + 0.235 * x * x * x)

    change_x = current.x - target.x
    change_y = current.y - target.y
    original_to = target

    max_change = max_speed * smoothTime

    max_change_sq = max_change * max_change
    sq_dist = change_x * change_x + change_y * change_y
    if sq_dist > max_change_sq:
        mag = float(math.sqrt(sq_dist))
        change_x = change_x / mag * max_change
        change_y = change_y / mag * max_change
    
    target.x = current.x - change_x
    target.y = current.y - change_y

    temp_x = (current_velocity.x + omega * change_x) * delta_time
    temp_y = (current_velocity.y + omega * change_y) * delta_time

    current_velocity.x = (current_velocity.x - omega * temp_x) * exp
    current_velocity.y = (current_velocity.y - omega * temp_y) * exp

    output_x = target.x + (change_x + temp_x) * exp
    output_y = target.y + (change_y + temp_y) * exp

    # Prevent overshooting the target position
    orig_minus_cur_x = original_to.x - current.x
    orig_minus_cur_y = original_to.y - current.y
    out_minus_orig_x = output_x - original_to.x
    out_minus_orig_y = output_y - original_to.y

    if orig_minus_cur_x * out_minus_orig_x + orig_minus_cur_y * out_minus_orig_y > 0:
        output_x = original_to.x
        output_y = original_to.y

        current_velocity.x = (output_x - original_to.x) / delta_time
        current_velocity.y = (output_y - original_to.y) / delta_time
    return pygame.math.Vector2(output_x, output_y)