from game_body.battle import Body
from game_body.pause import Pause
from statistic.game import StatisticsParameters
from statistic.game import GameParameters
import os


class Menu(Body):
    def __init__(self):
        Body.__init__(self)
        self.create_table()
        self.greetings()
    
    def greetings(self):
        print('Добро пожаловать в числовую угадайку!')
        print("Вы в главном меню \n"
              "Нажмите на клавишу для активации действия:")
        print('1 - Начать игру\n2 - Выбрать уровень сложности\n3 - Статистика по всем играм\n4 - Завершить игру')
        self.number = int(input('Введите одно из предложенных чисел: '))
        if self.number == 1:
            self.start()
        elif self.number == 2:
            msg = input('В разработке, нажмите д для выхода в меню игры ')
            if msg == 'д':
                Menu()
        elif self.number == 3:
            self.choose_statistic_option()
        elif self.number == 4:
            self.exit()
    
    def start(self):
        self.clear_screen()
        if not self.get_max_game_number()[0][0]:
            self.game_number += 1
        else:
            self.game_number = self.get_max_game_number()[0][0] + 1
        print('Вы в игре! Для того, чтобы поставить на паузу, напишите слово "пауза" в командной строке')
        self.battle_process()
        return Menu()
    
    def choose_statistic_option(self):
        self.clear_screen()
        print('\nВ этом меню у Вас есть возможность посмотреть статистику по всем играм')
        if self.get_max_game_number()[0][0] is not None:
            print('Количество игр, сыгранных пользователем: %d \n\n' % (self.get_max_game_number()[0][0]))
        else:
            print('Вы пока не играли')
        print('Доступные запросы:')
        print('1 - Вывести статистику по всем играм')
        print('2 - Очитсить статистику')
        print('3 - Выйти в главное меню')
        self.number = int(input('\n\nВведите одно из предложенных чисел: '))
        if self.number == 1:
            self.clear_screen()
            res_query = self.show_data()
            self.convert_game_statistics_to_dict(res_query)
            print('Статистика по играм:\n')
            print(self.get_statistic_game_data_in_table())
            main_menu = input('Нажмите д, для выхода в меню статистики: ')
            if main_menu == 'д':
                return self.choose_statistic_option()
        elif self.number == 2:
            self.close_connection()
            os.remove('GuessGame1.db')
            print('Статистика очищена!')
            main_menu = input('Нажмите д, для выхода в главное меню: ')
            if main_menu == 'д':
                return Menu().greetings()
        elif self.number == 3:
            return Menu().greetings()
                
            
    
    def restart(self):
        self.clear_screen()
        restart_flag = False
        msg = input('Вы действительно хотите перезагрузить игру? (д/н) ')
        if msg == 'д':
            self.attempts = 0
            self.comp_number = 1
            self.result_status = {}
            self.battle_process()
            restart_flag = True
        elif msg == 'н':
            self.battle_process()
        return restart_flag


if __name__ == '__main__':
    sh = Menu()
    sh.choose_statistic_option()
