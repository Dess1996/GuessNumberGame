from limitations.user_number import CheckUserAction
from generator.generate_computer_number import GenerateComputerNumber

import sys
import pandas as pd
from tabulate import tabulate
from limitations.limits import UserLimit
from game_body.pause import Pause

from generator.generate_computer_number import GenerateComputerNumber
from statistic.game import StatisticsParameters


class Body(UserLimit, Pause):
    def __init__(self):
        UserLimit.__init__(self)
        Pause.__init__(self)
    
    def computing_checking_parameters(self):
        self.check_on_number()
        self.check_on_actions()
        self.check_on_pause()
        if self.is_check_number:
            print('Ты прошёл все проверки!')
        elif self.is_check_pause:
            return self.pause()
        else:
            print('Я принимаю значения только от 0 до 100')
            return self.is_exit()
    
    def create_new_attempt(self):
        self.attempts += 1
        self.set_user_number()
        self.computing_checking_parameters()
        if self.comp_number == 1:
            print('Теперь я загадываю')
            self.get_computer_number()
    
    def battle_process(self):
        while self.comp_number != self.user_action:
            if self.comp_number > int(self.user_action):
                self.battle_result = 'Не угадал! Моё число больше!'
                print(self.battle_result)
                self.attempts += 1
                self.write_statistics_data()
                self.set_user_number()
                self.computing_checking_parameters()
            elif self.comp_number < int(self.user_action):
                self.battle_result = 'Не угадал! Моё число число меньше!'
                self.attempts += 1
                print(self.battle_result)
                self.write_statistics_data()
                self.set_user_number()
                self.computing_checking_parameters()
            else:
                self.battle_result = 'Поздравляем! Вы угадали за %d попыток' % self.attempts
                print(self.battle_result)
                self.exit()
    
    def write_statistics_data(self):
        self.result_status[self.attempts] = {}
        self.result_status[self.attempts]['попытка'] = str(self.attempts)
        self.result_status[self.attempts]['результат'] = self.battle_result
        self.result_status[self.attempts]['введённое пользователем значение'] = self.user_action
    
    def get_statistics(self):
        df = pd.DataFrame.from_dict(self.result_status).T
        df = df.set_index('попытка')
        return tabulate(df, headers='keys', tablefmt='psql')
    
    def pause(self):
        self.clear_screen()
        print('Игра на паузе \n'
              'Выберете действие, которое хотите посмотреть\n\n'
              '1 - Продолжить игру\n'
              '2 - Перезагрузить игру\n'
              '3 - Посмотреть статистику игры\n'
              '4 - Завершить игру')
        menu_number = int(input('Выберете действие: '))
        if menu_number == 1:
            self.is_check_pause = False
            self.battle_process()
        elif menu_number == 2:
            self.restart()
        elif menu_number == 3:
            print(self.get_statistics())
            msg = input('Нажмите д, чтобы выйти в меню паузы: ')
            if msg == 'д':
                return self.pause()
        elif menu_number == 4:
            if not self.is_exit():
                self.battle_process()
    
    def is_exit(self):
        msg = input('Желаете выйти из игры? (д/н)')
        if msg == 'д':
            return self.exit()
        else:
            return self.battle_process()
    
    def get_computer_number(self):
        com_number = GenerateComputerNumber()
        self.comp_number = com_number.computer_number
    
    def exit(self):
        print('Пока')
        sys.exit(0)
