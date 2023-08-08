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
    
    def get_statistics_session_data_in_table(self):
        df = pd.DataFrame.from_dict(self.session_status).T
        df = df.set_index('попытка')
        return tabulate(df, headers='keys', tablefmt='psql')
    
    def get_statistic_game_data_in_table(self):
        df = pd.DataFrame.from_dict(self.game_statistic).T
        return tabulate(df, headers='keys', tablefmt='psql')
    
    def write_game_statistics(self):
        for try_id, values in self.session_status.items():
            self.game_statistic[try_id] = {}
            self.game_statistic[try_id]['номер игры'] = self.game_number
            self.game_statistic[try_id]['загаданное число компьютера'] = self.comp_number
            for item, value in values.items():
                self.game_statistic[try_id][item] = value
   
    def convert_game_statistics_to_dict(self, data):
        self.game_statistic = {}
        row = 1
        for i in data:
            self.game_statistic[row] = {}
            self.game_statistic[row]['номер игры'] = i[0]
            self.game_statistic[row]['попытка'] = i[1]
            self.game_statistic[row]['число компьютера'] = i[2]
            self.game_statistic[row]['число пользователя'] = i[3]
            self.game_statistic[row]['статус'] = i[4]
            row += 1
        return self.game_statistic
            
            
        
    
    