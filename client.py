import pygame
import socket
import pickle
from graphicshandler import GraphicsHandler

server = "25.3.219.121"  # IPV4 Address
port = 5555
width = 1440
height = 900

fps = 60
graphics_handler = GraphicsHandler()


class Network:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.address = (self.server, self.port)
        self.player = self.connect()

    def get_player(self):
        return self.player

    def connect(self):
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(2048))
        except:
            print("Error while connecting")

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)


def game_loop():
    clock = pygame.time.Clock()
    running = True
    network = Network()
    player = network.get_player()

    while running:
        # Only run the game loop fps times per second
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        mouse_position = pygame.mouse.get_pos()
        player.update_turret_rotation((mouse_position[0] - width//2, mouse_position[1] - height//2))
        player.move()
        data = network.send(player)

        graphics_handler.update_display(data, player.x, player.y)


if __name__ == "__main__":
    game_loop()
