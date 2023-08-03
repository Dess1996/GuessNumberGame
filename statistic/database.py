from statistic.game import Statistics

import sqlite3


class DataBase(Statistics):
    def __init__(self):
        Statistics.__init__(self)
        self.con = sqlite3.connect("GuessGame1.db")
        self.cur = self.con.cursor()
    
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


class GameQuery(DataBase):
    def __init__(self):
        DataBase.__init__(self)
    
    def get_max_game_number_id(self):
        res = self.cur.execute("""SELECT MAX(game_number_id) FROM results""")
        return res.fetchone()
    
    def get_max_game_number(self):
        res = self.cur.execute("""SELECT MAX(game_number) FROM game""")
        return res.fetchall()
    
    def write_data_game_statistics(self, data):
        max_game_id = self.get_max_game_number_id()[0]
        for i, j in data.items():
            self.cur.execute("INSERT INTO computer(computer_number) VALUES (?)", (j['загаданное число компьютера'],))
            self.cur.execute("INSERT INTO user(user_number) VALUES (?)", (j['введённое пользователем значение'],))
            self.cur.execute("INSERT INTO game(game_number, try ) VALUES (?, ?)", (j['номер игры'], j['попытка']))
            max_game_id += 1
            self.cur.execute("INSERT INTO results(user_number_id, computer_number_id, game_number_id, status) "
                             "VALUES (?, ?, ?, ?)", (i, i, str(max_game_id), j['результат']))
        
        self.con.commit()
    
    def show_data(self):
        res = self.cur.execute("""
        SELECT game.game_number, game.try, computer.computer_number, user.user_number, results.status
            FROM results
        JOIN computer ON computer.id = results.computer_number_id
        JOIN user ON user.id = results.user_number_id
        JOIN game ON game.id = results.game_number_id
        """)
        return res.fetchall()


if __name__ == '__main__':
    db = DataBase()
    #    db.create_table()
    #    db.write_data()
    for i in db.show_data():
        print(i)
