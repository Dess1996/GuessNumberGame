import sqlite3


class DataBase:
    def __init__(self):
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
        
    def write_data(self):
        pass


if __name__ == '__main__':
    db = DataBase()
    db.create_table()
