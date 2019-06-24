import socket
from _thread import *
from tank import Tank
import pickle
from random import randint

server = "192.168.0.113"  # IPV4 Address
port = 5555  # 5555

players = []


def threaded_client(connection, player):
    print("connected to player", player)
    connected = True
    new_tank = Tank(100, 100, 10, (randint(0, 255), randint(0, 255), randint(0, 255)))
    players.append(new_tank)
    connection.send(pickle.dumps(new_tank))

    while connected:
        try:
            data = pickle.loads(connection.recv(4096))  # Increasing bits lowers speed
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                reply = players

            connection.sendall(pickle.dumps(reply))

        except:
            connected = False
    print("Lost connection to player ", player)
    connection.close()


if __name__ == "__main__":
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
    while listening:
        connection, address = s.accept()
        print("Connected to", address)

        start_new_thread(threaded_client, (connection, current_player))
        current_player += 1
