import math

# A method (function) for the bullet class

def _set_velocity(self, turret_x, turret_y, asteroid_x, asteroid_y, bullet_speed):
	def assess_direction(turret_xy, asteroid_xy):
		if turret_xy < asteroid_xy:
			return 1
		elif turret_xy > asteroid_xy:
			return -1
		else:
			return 0
	try:
		slope = (turret_y - asteroid_y) / (turret_x - asteroid_x)
		angle = math.atan(slope)
		velocity_x = math.cos(angle) * assess_direction(turret_x, asteroid_x) * bullet_speed
		velocity_y = math.sin(angle) * assess_direction(turret_x, asteroid_x) * bullet_speed
		
	except ZeroDivisionError:
		velocity_x = 0
		velocity_y = assess_direction(turret_y, asteroid_y) * bullet_speed

	return velocity_x, velocity_y
