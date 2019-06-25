import pygame
from sprites import SpritesContainer
from math import degrees
width = 1440
height = 900


class GraphicsHandler:
	def __init__(self):
		self.x_offset = 0
		self.y_offset = 0
		self.sprites_container = SpritesContainer()
		self.screen = pygame.display.set_mode((width, height))

	def update_display(self, data, x_offset, y_offset):
		self.x_offset = x_offset
		self.y_offset = y_offset
		self.screen.fill((0, 0, 0))
		self.draw_tanks(data["tanks"])
		pygame.display.update()

	def draw_tanks(self, tank_data):
		for tank in tank_data.values():
			self.draw_tank_body(tank.x - self.x_offset + width//2, tank.y - self.y_offset + height//2, tank.body_rotation, tank.tank_body_model)

	def draw_tank_body(self, x: int, y: int, body_rotation: float, body_model: str):
		body_image = self.sprites_container.tank_body_sprites[body_model]
		body_image = pygame.transform.rotate(body_image, degrees(body_rotation))
		image_size = body_image.get_size()
		self.screen.blit(body_image,  (x - image_size[0] // 2, y - image_size[1] // 2))
