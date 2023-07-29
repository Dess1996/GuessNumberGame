from game_statistic.session import GameParameters


class GenerateUserAction(GameParameters):
    def __init__(self):
        GameParameters.__init__(self)
    
    def set_user_number(self):
        self.user_action = input('Попытка %d. Загадайте число от 1 до 100...' % self.attempts)
        self.my_numbers.append(self.user_action if self.user_action.isalpha() else None)
