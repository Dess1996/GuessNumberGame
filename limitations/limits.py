from generator.generate_user_number import User
from statistic.game import CheckParameters


class UserLimit(CheckParameters, User):
    def __init__(self):
        CheckParameters.__init__(self)
        User.__init__(self)

    def check_on_actions(self):
        if not self.is_check_pause and not self.is_check_number:
            self.is_check_letters = True
        else:
            self.is_check_letters = False

    def check_on_pause(self):
        if self.user_action == 'п':
            self.is_check_pause = True
        else:
            self.is_check_pause = False

    def check_on_number(self):
        if self.user_action.isdigit() and int(self.user_action) <= 100:
            self.is_check_number = True
        else:
            self.is_check_number = False
    