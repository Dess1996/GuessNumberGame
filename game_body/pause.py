import os
import sys


from statistic.game import CheckParameters
from statistic.database import DataBase


class Pause(CheckParameters, DataBase):
    def __init__(self):
        CheckParameters.__init__(self)
        DataBase.__init__(self)
    
    def get_pause(self):
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
            print(self.get_session_statistics_data())
            msg = input('Нажмите д, чтобы выйти в меню паузы: ')
            if msg == 'д':
                return self.get_pause()
        elif menu_number == 4:
            if not self.is_exit():
                self.battle_process()
    
    def is_exit(self):
        msg = input('Желаете выйти из игры? (д/н)')
        if msg == 'д':
            return self.exit()
        else:
            return self.battle_process()
    
    def clear_screen(self):
        return os.system('cls')
    
    def exit(self):
        print('Пока')
        sys.exit(0)
