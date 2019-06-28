import pygame
import socket
import pickle
from projectiles import Bullet
from graphicshandler import GraphicsHandler
from menu import create_menu
from math import sin, cos

port = 5555
width = 1440
height = 900


class Network:
    def __init__(self, server_address: str) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server_address
        self.port = port
        self.address = (self.server, self.port)

    def connect(self):
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(4096))
        except:
            print("Error while connecting")
            return None, None

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*5))
        except:
            print("Lost connection to server")
            return None


def game_loop(server_address: str, player_name: str) -> None:
    fps = 60
    clock = pygame.time.Clock()
    running = True
    network = Network(server_address)
    player, trees = network.connect()
    if not player:
        print("No response from server")
        return None

    graphics_handler = GraphicsHandler()
    turret_reload_speed = 90
    turret_reload_cooldown = 0

    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return None

        mouse_position = pygame.mouse.get_pos()
        player.update_turret_rotation((mouse_position[0] - width//2, mouse_position[1] - height//2))
        keys = pygame.key.get_pressed()
        if keys is not None:
            player.move(keys)

        mouse_pressed = pygame.mouse.get_pressed()
        new_bullet = None
        if mouse_pressed[0] and turret_reload_cooldown == 0:
            new_bullet = Bullet(player.x + 60 * cos(player.turret_rotation), player.y - 60 * sin(player.turret_rotation), player.turret_rotation)
            turret_reload_cooldown = turret_reload_speed

        if turret_reload_cooldown != 0:
            turret_reload_cooldown -= 1

        data = network.send((player, new_bullet))
        if data:
            graphics_handler.update_display(data, player.x, player.y, trees)
        else:
            running = False


if __name__ == "__main__":
    run_game, server_address, player_name = create_menu()
    if run_game:
        game_loop(server_address, player_name)
