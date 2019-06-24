import socket
from _thread import *
from tank import Tank
import pickle
from typing import Tuple

server = "192.168.0.113"  # IPV4 Address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)  # Two connections maximum (2 players)
print("Listening for connection")

players = [Tank(0, 0, 5, (0, 255, 0)), Tank(100, 100, 5, (0, 0, 255))]


def threaded_client(connection, player):
    print("connected player ", player)
    connected = True
    connection.send(pickle.dumps(players[player]))

    while connected:
        try:
            data = pickle.loads(connection.recv(4096))  # Increasing bits lowers speed
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

            connection.sendall(pickle.dumps(reply))

        except:
            connected = False
    print("Lost connection")
    connection.close()


current_player = 0
while True:
    connection, address = s.accept()
    print("Connected to", address)

    start_new_thread(threaded_client, (connection, current_player))
    current_player += 1
