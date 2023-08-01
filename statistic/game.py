import sqlite3


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect("GuessGame1.db")
        self.cur = self.con.cursor()
        self.com_number = 55  # TODO: пока число компьютера константа
        self.game_number = 1  # TODO:  пока номер игры константа
    
    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS user
        (
            id integer PRIMARY KEY AUTOINCREMENT,
            user_number integer
            
        )
        """)
        
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS computer
        (
            id integer PRIMARY KEY AUTOINCREMENT,
            computer_number integer
        )
        """)
        
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS game
        (
            id integer PRIMARY KEY AUTOINCREMENT,
            game_number integer,
            try integer
            
        )
        """)
        
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS results
                (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    
                    user_number_id integer,
                    computer_number_id integer,
                    game_number_id integer,
                    status text,
                    
                    FOREIGN KEY (user_number_id) REFERENCES user(id),
                    FOREIGN KEY (computer_number_id) REFERENCES computer(id),
                    FOREIGN KEY (game_number_id) REFERENCES game(id)
                    
                    
                )
                """)
        self.con.commit()
    
    def get_max_game_number(self):
        res = self.cur.execute("""
        SELECT
            game_number
        FROM
            game
        WHERE
            game_number = (SELECT MAX(game_number) FROM game);
        
        """)
        res.fetchall()
        return res
    
    def write_data(self):
        for i, j in data.items():
            self.cur.execute("INSERT INTO computer(computer_number) VALUES (?)", (str(self.com_number),))
            self.cur.execute("INSERT INTO user(user_number) VALUES (?)", (j['введённое пользователем значение'],))
            self.cur.execute("INSERT INTO game(game_number, try ) VALUES (?, ?)", (self.game_number, j['попытка']))
            self.cur.execute("INSERT INTO results(user_number_id, computer_number_id, game_number_id, status  ) "
                             "VALUES (?, ?, ?, ?)", (i, i, i, j['результат']))
        self.con.commit()
    
    def show_data(self):
        res = self.cur.execute("""
        SELECT game.try, computer.computer_number, user.user_number, game.game_number, results.status
            FROM results
        JOIN computer ON computer.id = results.computer_number_id
        JOIN user ON user.id = results.user_number_id
        JOIN game ON game.id = results.game_number_id
        """)
        return res.fetchall()


data = {1: {'попытка': '1', 'результат': 'Не угадал! Моё число больше!', 'введённое пользователем значение': '55'},
        2: {'попытка': '2', 'результат': 'Не угадал! Моё число число меньше!',
            'введённое пользователем значение': '67'},
        3: {'попытка': '3', 'результат': 'Не угадал! Моё число число меньше!',
            'введённое пользователем значение': '88'}}

if __name__ == '__main__':
    db = DataBase()
    #    db.create_table()
    #    db.write_data()
    print(db.show_data())
