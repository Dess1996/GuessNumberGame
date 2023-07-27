from generator.generate_user_number import GenerateUserAction


class CheckUserAction(GenerateUserAction):
    def __init__(self):
        GenerateUserAction.__init__(self)
        self.check_ok = False
        self.on_pause = False
    
    def check_number(self):
        if self.user_number == 'пауза':
            self.on_pause = True
        else:
            if int(self.user_number) <= 100:
                self.check_ok = True
        
