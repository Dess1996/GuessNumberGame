from statistic.game import StatisticsParameters


class User(StatisticsParameters):
    def __init__(self):
        StatisticsParameters.__init__(self)

    def set_user_number(self):
        self.user_action = input('Попытка %d. Загадайте число от 1 до 100...' % self.attempts)
