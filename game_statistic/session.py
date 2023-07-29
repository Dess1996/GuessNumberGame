from dataclasses import dataclass


@dataclass
class Statistics:
    my_numbers = []
    user_number = 0
    comp_number = 1
    attempts = 1


@dataclass
class GameParameters(Statistics):
    menu_number = 0
    on_pause = False
    on_exit = False
    check_ok = False
