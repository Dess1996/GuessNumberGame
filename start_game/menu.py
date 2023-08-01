from game_body.battle import Body

import os


class Menu(Body):
    def __init__(self):
        Body.__init__(self)
        print('Добро пожаловать в числовую угадайку!')
        print("Вы в главном меню \n"
              "Нажмите на клавишу для активации действия:")
        print('1 - Начать игру\n2 - Статистика по всем играм\n3 - Завершить игру')
        self.number = int(input('Введите одно из предложенных чисел: '))
        if self.number == 1:
            self.start()
        elif self.number == 2:
            print('Статистика по всем играм пока недоступна')  # TODO: сделать статистику по всем играм
        elif self.number == 3:
            self.exit()

    def start(self):
        self.clear_screen()
        if not self.db.get_max_game_number():
            self.game_number += 1
        else:
            self.game_number = self.db.get_max_game_number()[0][0] + 1
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
    
    def clear_screen(self):
        return os.system('cls')
