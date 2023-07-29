from limitations.user_number import CheckUserAction
from generator.generate_user_number import GenerateUserAction
from generator.generate_computer_number import GenerateComputerNumber
import sys


class Body(CheckUserAction):
    def __init__(self):
        CheckUserAction.__init__(self)
    
    def check_limitation(self):
        if int(self.user_number) < 100:
            print('Проверка прошла успешно')
            self.check_ok = True
        else:
            print('Я жду от вас целое число от 1 до 100!')
    
    def set_and_check_number(self):
        self.set_user_number()
        if self.user_number == 'п':
            return self.pause()
        else:
            return self.check_limitation()
    
    def battle_process(self):
        self.set_and_check_number()
        if not self.check_ok:
            return self.is_exit()
        else:
            print('Хорошо, ты справился! Теперь я подумаю...')
            if self.comp_number == 1:
                self.get_computer_number()
            while self.comp_number != self.user_number:
                self.attempts += 1
                if self.comp_number > int(self.user_number):
                    print('Не угадал! Моё число больше!')
                    self.set_and_check_number()
                elif self.comp_number < int(self.user_number):
                    print('Не угадал! Моё число число меньше!')
                    self.set_and_check_number()
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
        self.menu_number = int(input('Выберете действие: '))
        if self.menu_number == 1:
            self.on_pause = False
            self.battle_process()
        elif self.menu_number == 2:
            self.restart()
        elif self.menu_number == 3:  # TODO: Доработать статистику, скорее всего понадобится создать новый класс
            msg = input('Статистика недоступна, нажмите д, чтобы выйти: ')
            if msg == 'д':
                return self.pause()
        elif self.menu_number == 4:
            if not self.is_exit():
                self.battle_process()
    
    def is_exit(self):
        exit_flag = False
        msg = input('Желаете выйти из игры? (д/н)')
        if msg == 'д':
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
        print('Пока')
        sys.exit(0)
