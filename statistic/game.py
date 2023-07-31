import sqlite3


class DataBase:
    def __init__(self):
        self.con = sqlite3.connect("GuessGame.db")
        self.cur = self.con.cursor()
    
    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS try_table
        (
            id integer PRIMARY KEY,
            number integer NOT NULL
        )
        """)
        
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS win_table
        (
            id integer PRIMARY KEY,
            is_win text
        )
        
        
        """)

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS statistic_game
        (
            id integer PRIMARY KEY,
            user_number integer,
            computer_number integer,
            result text
        )
        """)

        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS game_table
                (
                    id integer PRIMARY KEY,
                    game_number int
                )
                """)
        
        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS results
                (
                    id integer PRIMARY KEY,
                    try_table_id integer NOT NULL,
                    win_table_id integer NOT NULL,
                    statistic_game_id integer NOT NULL,
                    game_table_id integer NOT NULL,
                    
                    FOREIGN KEY (try_table_id) REFERENCES try_table(id),
                    FOREIGN KEY (win_table_id) REFERENCES win_table(id),
                    FOREIGN KEY (statistic_game_id) REFERENCES statistic_game(id),
                    FOREIGN KEY (game_table_id) REFERENCES game_table(id)
                    
                    
                )
                """)


if __name__ == '__main__':
    db = DataBase()
    db.create_table()
