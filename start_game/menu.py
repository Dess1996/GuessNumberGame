from limitations.user_number import CheckUserNumber
from generator.generate_user_number import GenerateUserNumber
from game_body.battle import Body


class Menu(Body):
    def __init__(self):
        Body.__init__(self)
    
    def start(self):
        print('Добро пожаловать в числовую угадайку')
        self.set_user_number()
        self.check_limitation()
        print('Хорошо, ты справился! Теперь я подумаю...')
        self.get_computer_number()
        self.is_begin_battle()
        self.battle_process()
    
    def restart(self):
        exit_flag = False
        msg = input('Сыграем снова? (да/нет) ')
        if msg == 'да':
            self.set_user_number()
            self.check_number()
            exit_flag = True
        return exit_flag
