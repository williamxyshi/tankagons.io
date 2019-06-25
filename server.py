import socket
from _thread import *
from tank import Tank
import pickle
from random import randint

server = "25.3.163.186"  # IPV4 Address
port = 5555  # 5555

data = {"tanks": {}}


def threaded_client(connection, player_number):
    print("connected to player", player_number)
    connected = True
    new_tank = Tank(100, 100, 10, (randint(0, 255), randint(0, 255), randint(0, 255)))
    data["tanks"][player_number] = new_tank
    connection.send(pickle.dumps(new_tank))

    while connected:
        try:
            received_data = pickle.loads(connection.recv(4096))  # Increasing bits lowers speed
            data["tanks"][player_number] = received_data

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
