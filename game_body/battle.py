from limitations.user_number import CheckUserAction
from generator.generate_user_number import GenerateUserAction
from generator.generate_computer_number import GenerateComputerNumber


class Body(CheckUserAction):
    def __init__(self):
        CheckUserAction.__init__(self)
        self.comp_number = 0
        self.menu_number = 0
        self.on_pause = False
    
    def check_limitation(self):
        self.check_number()
        while not self.check_ok:
            print('Я жду от вас целое число от 1 до 100!')
            if not self.restart():
                print('Пока!')
                break
        if self.check_ok:
            print('Проверка прошла успешно')
    
    def is_begin_battle(self):
        msg = input('Загадал! Начинаем битву?(да/нет) ')
        if msg == 'да':
            pass
        else:
            print('Ах ты трусишка')
            self.restart()
    
    def battle_process(self):
        while self.comp_number != self.user_number:
            if self.on_pause:
                return self.pause()
            self.attempts += 1
            if self.comp_number > int(self.user_number):
                print('Не угадал! Моё число больше!')
                if self.is_exit():
                    break
                self.set_user_number()
                self.check_limitation()
            elif self.comp_number < int(self.user_number):
                print('Не угадал! Моё число число меньше!')
                if self.is_exit():
                    break
                if self.set_user_number() == 'пауза':
                    self.pause()
                self.check_limitation()
            else:
                print('Поздравляем! Вы угадали за %d попыток' % self.attempts)
                
                self.restart()
    
    def pause(self):
        self.clear_screen()
        print('Игра на паузе \n'
              'Выберете действие, которое хотите посмотреть\n\n'
              '1 - Продолжить игру\n'
              '2 - Перезагрузить игру\n'
              '3 - Посмотреть статистику игры\n'
              '4 - Завершить игру')
        self.menu_number = int(input('Выберете действие: '))
        if self.menu_number == 1:
            self.set_user_number()
            self.check_number()
            self.battle_process()
        elif self.menu_number == 2:
            self.restart()
        elif self.menu_number == 3:
            print('Статистика недоступна')
        elif self.menu_number == 4:
            self.is_exit()
    
    def is_exit(self):
        self.clear_screen()
        exit_flag = False
        msg = input('Желаете выйти из игры? (да/нет)')
        if msg == 'да':
            return self.exit()
        return exit_flag
    
    def get_computer_number(self):
        com_number = GenerateComputerNumber()
        self.comp_number = com_number.computer_number
    
    def set_user_number(self):
        GenerateUserAction.set_user_number(self)
    
    def check_number(self):
        CheckUserAction.check_number(self)
    
    def exit(self):
        print('Пока!')
