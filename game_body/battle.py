from limitations.user_number import CheckUserAction
from generator.generate_user_number import GenerateUserAction
from generator.generate_computer_number import GenerateComputerNumber
import sys


class Body(CheckUserAction):
    def __init__(self):
        CheckUserAction.__init__(self)
    
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
    
    def battle_process(self):
        self.set_user_number()
        self.computing_checking_parameters()
        if self.comp_number == 1:
            print('Теперь я загадываю')
            self.get_computer_number()
        while self.comp_number != self.user_action:
            self.attempts += 1
            if self.comp_number > int(self.user_action):
                print('Не угадал! Моё число больше!')
                self.set_user_number()
                self.computing_checking_parameters()
            elif self.comp_number < int(self.user_action):
                print('Не угадал! Моё число число меньше!')
                self.set_user_number()
                self.computing_checking_parameters()
            else:
                self.attempts -= 1
                print('Поздравляем! Вы угадали за %d попыток' % self.attempts)
                self.exit()
    
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
        elif menu_number == 3:  # TODO: Доработать статистику, скорее всего понадобится создать новый класс
            msg = input('Статистика недоступна, нажмите д, чтобы выйти: ')
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
