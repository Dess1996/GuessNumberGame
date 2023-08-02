from dataclasses import dataclass
import pandas as pd
from tabulate import tabulate


@dataclass
class CheckParameters:
    on_exit = False
    is_check_number = False
    is_check_pause = False
    is_check_letters = False
    is_win = False


@dataclass
class StatisticsParameters:
    user_action = 0
    comp_number = 1
    attempts = 0
    battle_result = ''
    session_status = {}
    game_statistic = {}
    game_number = 0


@dataclass
class GameParameters:
    menu_number = 0


class Statistics(StatisticsParameters):
    def __init__(self):
        StatisticsParameters.__init__(self)
    
    def write_session_statistics_data(self):
        self.session_status[self.attempts] = {}
        self.session_status[self.attempts]['попытка'] = str(self.attempts)
        self.session_status[self.attempts]['результат'] = self.battle_result
        self.session_status[self.attempts]['введённое пользователем значение'] = self.user_action
    
    def get_session_statistics_data(self):
        df = pd.DataFrame.from_dict(self.session_status).T
        df = df.set_index('попытка')
        return tabulate(df, headers='keys', tablefmt='psql')
    
    def write_game_statistics(self):
        for try_id, values in self.session_status.items():
            self.game_statistic[try_id] = {}
            self.game_statistic[try_id]['номер игры'] = self.game_number
            self.game_statistic[try_id]['загаданное число компьютера'] = self.comp_number
            for item, value in values.items():
                self.game_statistic[try_id][item] = value
