from generator.generate_user_number import GenerateUserNumber


class CheckUserNumber(GenerateUserNumber):
    def __init__(self):
        GenerateUserNumber.__init__(self)
        self.check_ok = False
    
    def check_number(self):
        if self.user_number <= 100:
            self.check_ok = True
