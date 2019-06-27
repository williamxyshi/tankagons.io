from tkinter import *
from typing import Tuple


def create_menu() -> Tuple[bool, str, str]:
    run_game = False
    server_address = ""
    player_name = ""

    menu = Tk()
    menu.title("Tankagons")
    Label(menu, text="IPV4").grid(row=0)
    server_address_entry = Entry(menu)
    server_address_entry.grid(row=0, column=1)
    Label(menu, text="Name").grid(row=1)
    player_name_entry = Entry(menu)
    player_name_entry.grid(row=1, column=1)

    def handel_button_press():
        nonlocal run_game
        nonlocal server_address
        nonlocal player_name
        run_game = True
        server_address = server_address_entry.get()
        player_name = player_name_entry.get()
        menu.destroy()

    Button(menu, text="Confirm", command=lambda:  handel_button_press()).grid(row=2, column=0, sticky=W, pady=5)
    menu.mainloop()
    return run_game, server_address, player_name
