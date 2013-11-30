


def update_prick_position(new_direction, position, DISPLAY_SEGMENT):
    if new_direction == 'right':
        position[0] +=  1
        if position[0] >= DISPLAY_SEGMENT[0]:
            position[0] = 1
            
    elif new_direction == 'down':
        position[1] += 1
        if position[1] >= DISPLAY_SEGMENT[1]:
            position[1] = 1
			 
    elif new_direction == 'left':
        position[0] -= 1
        if position[0] <= 1:
            position[0] = DISPLAY_SEGMENT[0] - 1
			
    elif new_direction == 'up':
        position[1] -= 1
        if position[1] <= 1:
            position[1] = DISPLAY_SEGMENT[1] - 1

	return 
	
def prick_dis_pos(position, DISPLAY_SEGMENT_SIZE):
    return position*DISPLAY_SEGMENT_SIZE - DISPLAY_SEGMENT_SIZE/2
