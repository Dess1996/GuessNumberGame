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
        print('Вы в игре! Для того, чтобы поставить на паузу, напишите букву "п" в командной строке')
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
