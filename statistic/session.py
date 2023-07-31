from dataclasses import dataclass
import pandas as pd
from tabulate import tabulate


class SessionStatistics:
    def __init__(self):
        CheckParameters.__init__(self)
    
    def write_session_statistics_data(self):
        self.result_status[self.attempts] = {}
        self.result_status[self.attempts]['попытка'] = str(self.attempts)
        self.result_status[self.attempts]['результат'] = self.battle_result
        self.result_status[self.attempts]['введённое пользователем значение'] = self.user_action
    
    def get_session_statistics_data(self):
        df = pd.DataFrame.from_dict(self.result_status).T
        df = df.set_index('попытка')
        return tabulate(df, headers='keys', tablefmt='psql')


@dataclass
class CheckParameters(SessionStatistics):
    on_exit = False
    is_check_number = False
    is_check_pause = False
    is_check_letters = False
    is_win = False


@dataclass
class StatisticsSessionParameters(CheckParameters):
    user_action = 0
    comp_number = 1
    attempts = 0
    battle_result = ''
    result_status = {}


@dataclass
class GameParameters(StatisticsSessionParameters):
    menu_number = 0
