import pygame

def get_key(keys, read_time, player):
    if player == 1:
        if read_time == 0:
            return keys[pygame.K_z]
        elif read_time == 1:
            return keys[pygame.K_x]
        elif read_time == 2:
            return keys[pygame.K_SPACE]
        elif read_time == 3:
            return keys[pygame.K_RETURN]
        elif read_time == 4:
            return keys[pygame.K_UP]
        elif read_time == 5:
            return keys[pygame.K_DOWN]
        elif read_time == 6:
            return keys[pygame.K_LEFT]
        elif read_time == 7:
            return keys[pygame.K_RIGHT]
    elif player == 2:
        if read_time == 0:
            return keys[pygame.K_o]
        elif read_time == 1:
            return keys[pygame.K_p]
        elif read_time == 2:
            return keys[pygame.K_u]
        elif read_time == 3:
            return keys[pygame.K_i]
        elif read_time == 4:
            return keys[pygame.K_w]
        elif read_time == 5:
            return keys[pygame.K_s]
        elif read_time == 6:
            return keys[pygame.K_a]
        elif read_time == 7:
            return keys[pygame.K_d]
    else:
        raise Exception("Invalid player!")

def latch_controlers():
    pygame.event.poll()
    keys = pygame.key.get_pressed()

    return keys
