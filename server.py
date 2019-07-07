import socket
from _thread import *
from tank import Tank
from objects import Tree
import pickle
from random import randint
import pygame
import os
import queue

server = "25.3.163.186"  # IPV4 Address
port = 5555  # 5555

data = {"tanks": {}, "bullets": []}
trees = {}

tank_body_image_size = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets\\basetank.png')).get_size()
tank_damage = queue.Queue()


def threaded_client(connection, player_number):
    print("connected to player", player_number)
    connected = True
    new_tank = Tank(100, 100, 10, (randint(0, 255), randint(0, 255), randint(0, 255)), 'basic', 'basic', tank_body_image_size[0], tank_body_image_size[1])
    data["tanks"][player_number] = new_tank
    connection.send(pickle.dumps((new_tank, trees, player_number)))

    while connected:
        while not tank_damage.empty():
            damage_info = tank_damage.get()
            data["tanks"][player_number] = damage_info[0].update_health(10)

        try:
            received_data = pickle.loads(connection.recv(4096))  # Increasing bits lowers speed
            data["tanks"][player_number] = received_data[0]
            if received_data[1]:
                data["bullets"].append(received_data[1])

            if not received_data:
                print("Disconnected")
                break
            else:
                reply = data

            connection.sendall(pickle.dumps(reply))

        except:
            connected = False

    data["tanks"].pop(player_number)
    print("Lost connection to player ", player_number)
    connection.close()


def create_map(map_width: int, map_height: int):
    num_trees = randint(20, 40)
    for _ in range(num_trees):
        x = randint(20, map_width-20)
        y = randint(20, map_height-20)
        trees[(x, y)] = Tree(x, y, 0, randint(30, 50))


def server_loop():
    fps = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps)
        for bullet in data["bullets"]:
            if not bullet.update():
                for tank in data["tanks"].values():
                    if tank.detect_hit((bullet.x, bullet.y)):
                        data["bullets"].remove(bullet)
                        tank_damage.put((tank, bullet.damage))
                        print(tank.health)


if __name__ == "__main__":
    create_map(1500, 1500)

    # Create the server socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    # Enable socket to accept connections
    s.listen(0)
    print("Listening...")
    listening = True

    current_player = 0
    start_new_thread(server_loop, ())
    while listening:
        connection, address = s.accept()
        print("Connected to", address)

        start_new_thread(threaded_client, (connection, current_player))
        current_player += 1

