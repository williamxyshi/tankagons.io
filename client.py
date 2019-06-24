import pygame
import socket
import pickle
import time
from tank import Tank
from typing import Tuple

server = "192.168.0.113"  # IPV4 Address
port = 5555

fps = 60
width = 400
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tankagons")


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


def update_window(player1: Tank, player2: Tank) -> None:
    # Wipes the screen
    window.fill((0, 0, 0))
    player1.draw(window)
    player2.draw(window)


    pygame.display.update()


def game_loop():
    clock = pygame.time.Clock()
    running = True
    network = Network()
    player = network.get_player()
    while running:
        # Only run the game loop fps times per second
        clock.tick(fps)
        player2 = network.send(player)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        player.move()
        update_window(player, player2)


if __name__ == "__main__":
    game_loop()
