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
		pygame.display.set_caption("Tankagons")

	def update_display(self, data, x_offset, y_offset):
		self.draw_background()
		self.x_offset = x_offset
		self.y_offset = y_offset
		self.draw_tanks(data["tanks"])
		self.draw_bullets(data["bullets"])
		pygame.display.update()

	def draw_background(self):
		self.screen.blit(self.sprites_container.background_sprite, (0, 0))

	def draw_tanks(self, tank_data):
		for tank in tank_data.values():
			self.draw_tank_body(tank.x - self.x_offset + width//2, tank.y - self.y_offset + height//2, tank.body_rotation, tank.tank_body_model)
			self.draw_tank_turret(tank.x - self.x_offset + width//2, tank.y - self.y_offset + height//2, tank.turret_rotation, tank.tank_turret_model)

	def draw_bullets(self, bullet_data):
		for bullet in bullet_data:
			self.draw_bullet(bullet.x - self.x_offset + width//2, bullet.y - self.y_offset + height//2, bullet.bullet_angle)

	def draw_bullet(self, x: int, y: int, bullet_angle: int):
		bullet_image = self.sprites_container.bullet_sprites['bullet']
		bullet_image = pygame.transform.rotate(bullet_image, degrees(bullet_angle))
		image_size = bullet_image.get_size()
		self.screen.blit(bullet_image, (x - image_size[0] // 2, y - image_size[1] // 2))

	def draw_tank_turret(self, x: int, y: int, turret_rotation: float, turret_model: str):
		print(turret_rotation)
		turret_image = self.sprites_container.tank_turret_sprites[turret_model]
		turret_image = pygame.transform.rotate(turret_image, degrees(turret_rotation))
		image_size = turret_image.get_size()
		self.screen.blit(turret_image, (x - image_size[0] // 2, y - image_size[1] // 2))

	def draw_tank_body(self, x: int, y: int, body_rotation: float, body_model: str):
		body_image = self.sprites_container.tank_body_sprites[body_model]
		body_image = pygame.transform.rotate(body_image, degrees(body_rotation))
		image_size = body_image.get_size()
		self.screen.blit(body_image,  (x - image_size[0] // 2, y - image_size[1] // 2))
