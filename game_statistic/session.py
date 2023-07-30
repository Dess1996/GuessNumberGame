from dataclasses import dataclass


@dataclass
class CheckParameters:
    on_exit = False
    is_check_number = False
    is_check_pause = False
    is_check_letters = False


@dataclass
class Statistics(CheckParameters):
    user_action = 0
    comp_number = 1
    attempts = 0
    battle_result = ''
    result_status = {}


@dataclass
class GameParameters(Statistics):
    menu_number = 0
