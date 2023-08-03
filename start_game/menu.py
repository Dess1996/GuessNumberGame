from game_body.battle import Body
from game_body.pause import Pause
from statistic.game import StatisticsParameters
from statistic.game import GameParameters


class Menu(Body):
    def __init__(self):
        Body.__init__(self)
        self.create_table()
        self.greetings()
    
    def greetings(self):
        print('Добро пожаловать в числовую угадайку!')
        print("Вы в главном меню \n"
              "Нажмите на клавишу для активации действия:")
        print('1 - Начать игру\n2 - Статистика по всем играм\n3 - Завершить игру')
        self.number = int(input('Введите одно из предложенных чисел: '))
        if self.number == 1:
            self.start()
        elif self.number == 2:
            for i in self.show_data():
                print(i)
        elif self.number == 3:
            self.exit()
    
    def start(self):
        self.clear_screen()
        if not self.get_max_game_number()[0][0]:
            self.game_number += 1
        else:
            self.game_number = self.get_max_game_number()[0][0] + 1
        print('Вы в игре! Для того, чтобы поставить на паузу, напишите слово "пауза" в командной строке')
        self.battle_process()
    
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
