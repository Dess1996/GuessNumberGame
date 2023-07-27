class GenerateUserAction:
    def __init__(self):
        self.user_number = 0
        self.attempts = 1
    
    def set_user_number(self):
        self.user_number = input('Попытка %d. Загадайте число от 1 до 100...' % self.attempts)
