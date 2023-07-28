from limitations.user_number import CheckUserAction
from generator.generate_user_number import GenerateUserAction
from game_body.battle import Body
import os


class Menu(Body):
    def __init__(self):
        Body.__init__(self)
        print('Добро пожаловать в числовую угадайку!')
        print("Вы в главном меню \n"
              "Нажмите на клавишу для активации действия:")
        print('1 - Начать игру\n2 - Завершить игру')
        self.number = int(input('Введите одно из предложенных чисел: '))
        if self.number == 1:
            self.start()
        elif self.number == 2:
            self.exit()
    
    def start(self):
        self.clear_screen()
        print('Вы в игре! Для того, чтобы поставить на паузу, напишите слово "пауза" в командной строке')
        self.battle_process()
    
    def restart(self):
        self.clear_screen()
        restart_flag = False
        msg = input('Вы действительно хотите перезагрузить игру? (да/нет) ')
        if msg == 'да':
            self.attempts = 1
            self.comp_number = 1
            self.set_and_check_number()
            restart_flag = True
        elif msg == 'нет':
            self.set_user_number()
            self.check_number()
        return restart_flag
    
    def clear_screen(self):
        return os.system('cls')
