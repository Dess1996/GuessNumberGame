from limitations.user_number import CheckUserNumber
from generator.generate_user_number import GenerateUserNumber
from generator.generate_computer_number import GenerateComputerNumber


class Body(CheckUserNumber):
    def __init__(self):
        CheckUserNumber.__init__(self)
        self.comp_number = 0
    
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
            if self.comp_number > self.user_number:
                print('Не угадал! Моё число больше!')
                if self.is_exit():
                    break
                self.set_user_number()
                self.check_limitation()
            elif self.comp_number < self.user_number:
                print('Не угадал! Моё число число меньше!')
                if self.is_exit():
                    break
                self.set_user_number()
                self.check_limitation()
            else:
                print('О, ты выиграл!')
                self.restart()
    
    def is_exit(self):
        exit_flag = False
        msg = input('Желаете выйти из игры? (да/нет)')
        if msg == 'да':
            exit_flag = True
        return exit_flag
    
    def get_computer_number(self):
        com_number = GenerateComputerNumber()
        self.comp_number = com_number.computer_number
    
    def set_user_number(self):
        GenerateUserNumber.set_user_number(self)
    
    def check_number(self):
        CheckUserNumber.check_number(self)
