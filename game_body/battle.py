from limitations.limits import UserLimit
from game_body.pause import Pause

from generator.generate_computer_number import GenerateComputerNumber
from statistic.game import StatisticsParameters


class Body(UserLimit, Pause):
    def __init__(self):
        UserLimit.__init__(self)
        Pause.__init__(self)
    
    def computing_checking_parameters(self):
        self.check_on_number()
        self.check_on_actions()
        self.check_on_pause()
        if self.is_check_number:
            print('Ты прошёл все проверки!')
        elif self.is_check_pause:
            return self.get_pause()
        else:
            print('Я принимаю значения только от 0 до 100')
            return self.is_exit()
    
    def create_new_attempt(self):
        self.attempts += 1
        self.set_user_number()
        self.computing_checking_parameters()
        if self.comp_number == 1:
            print('Теперь я загадываю')
            self.get_computer_number()
        if self.comp_number > int(self.user_action):
            self.battle_result = 'Не угадал! Моё число больше!'
            self.write_session_statistics_data()
        elif self.comp_number < int(self.user_action):
            self.battle_result = 'Не угадал! Моё число число меньше!'
            print(self.battle_result)
            self.write_session_statistics_data()
        else:
            self.battle_result = 'Поздравляем! Вы угадали за %d попыток' % self.attempts
            self.write_session_statistics_data()
    
    def battle_process(self):
        while str(self.comp_number) != self.user_action:
            self.create_new_attempt()
        self.write_game_statistics()
        self.write_data_game_statistics(data=self.game_statistic)
        self.exit()
    
    def get_computer_number(self):
        com_number = GenerateComputerNumber()
        self.comp_number = com_number.computer_number

if __name__ == '__main__':
    bd = Body()
    bd.battle_process()